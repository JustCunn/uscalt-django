import requests

from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from .models import Room, RoomLink, MainSilo, AuxSilo #LinkRegularData
from .serializers import RoomInfoSerializer, RoomLinkSerializer, RegisterRoom, MainSiloSerializer, AuxSiloSerializer, RoomInfoNoUsersSerializer #LinkRegularDataSerializer
from accounts.serializers import UserSerializer
from django.contrib.auth.models import User
from django.http import HttpResponse
from io import StringIO
import hashlib

import ast
import csv
from datetime import datetime, date, timezone
import requests
import random  
import string  

class RoomApi(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('name')
    lookup_field = 'name'
    serializer_class = RoomInfoSerializer

class RegisterRoom(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RegisterRoom

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RegisterLink(generics.ListCreateAPIView):
    """Create a Link"""
    queryset = RoomLink.objects.all()
    serializer_class = RoomLinkSerializer

    def perform_create(self, serializer):
        #main_silo = self.request.data.get('room')+self.request.data.get('display_name')+'silo'
        #ms = MainSilo(name=main_silo)
        #ms.save()
        print(self.request.data.get('off_id'))
        if self.request.data.get('off_id') == True:
            off_id = ''.join((random.choice(string.ascii_lowercase) for x in range(10)))
            serializer.save(name=self.request.data.get('room')+self.request.data.get('display_name'),
            off_id=off_id, url=self.request.data.get('url'))
        else:
            serializer.save(name=self.request.data.get('room')+self.request.data.get('display_name'))

class CheckIfExists(APIView):
    """Used by client-side devices to check if they need to send data in again"""
    def post(self, request, *args, **kwargs):
        #Check if the user already has data sent in
        #TODO Tell user not to send data in
        try:
            exist = AuxSilo.objects.get(name=request.data.get('name'))
        except AuxSilo.DoesNotExist:
            exist = None

        if exist is not None:
            aux = AuxSilo.objects.get(name=request.data.get('name'))
            u_time = aux.time
            if (datetime.now(timezone.utc) - u_time).seconds > 7200:
                response = Response({"status": "true"}, {"hash": aux.data_hash})
            else:
                response = Response({"status": "false"})
        else:
            response = Response({"status": "true"})
        
        return response

class UploadData(APIView):
    def post(self, request, *args, **kwargs):
        #If user silo already exists, replace the data
        if AuxSilo.objects.filter(name=request.data.get('name')).exists():
            d_hash = hashlib.md5(request.data.get('data').encode('UTF-8'))
            ax = AuxSilo.objects.filter(link=request.data.get('link'), time=datetime.now())
            ax.data_hash, ax.data = data_hash=d_hash, data=request.data.get('data')
            ax.save()
        else:
            #If not, Create a silo and temp store data
            d_hash = hashlib.md5(request.data.get('data').encode('UTF-8'))
            ax = AuxSilo(name=request.data.get('name'), data=request.data.get('data'), 
            link=request.data.get('link'), time=datetime.now(timezone.utc), data_hash=d_hash)
            ax.save()
        
        return Response({"task": "success"})
        
class BuyData(APIView):
    """Sets buying mechanism into work"""
    def post(self, request, *args, **kwargs):
        link = request.data.get('link')
        uid = request.data.get('id')

        #Get the required Room Link
        sought_room_link = RoomLink.objects.get(id=link)

        #Add the user to the 'waiting list' and tell devices the data is sought
        sought_room_link.buyers.add(User.objects.get(id=uid))
        sought_room_link.sought = True
        sought_room_link.save()

class DownloadData(APIView):
    """Bundles and sends download to user"""
    def get(self, request, *args, **kwargs):
        link = self.kwargs['link']
        uid = self.kwargs['uid']

        #Get the relevant Room Link
        sought_room_link = RoomLink.objects.get(id=link)
        fields = sought_room_link.fields.split(',')

        if sought_room_link.off_id is not None:
            
            r = requests.get(sought_room_link.url+'download/', params = {'off_id': sought_room_link.off_id,
            'fields': sought_room_link.fields})
            data = r.json()
            print(r.json())
            response = HttpResponse(data['file'], content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="somefile.csv"'
            """
            r = requests.get(sought_room_link.url+'download/', params = {'off_id': sought_room_link.off_id,
            'fields': sought_room_link.fields})
            """
        else:
            #Get all the associated silos
            Auxs = AuxSilo.objects.filter(link=sought_room_link.display_name)

            temp_list = []
            
            for item in Auxs:
                temp_list.append(item.data.split(','))

            
            #Turn into downloadable file
            response = HttpResponse(
                content_type='text/csv',
                headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
            )

            write = csv.writer(response)
            write.writerow(fields)

            for i in temp_list:
                write.writerow(i)

            Auxs.delete()
            
        sought_room_link.buyers.remove(User.objects.get(id=uid))

        #Remove the data from our server
        #print(sought_room_link.buyers)
        #if sought_room_link.buyers is None:
        sought_room_link.sought = False

        sought_room_link.save()

        return response


"""
class RetrieveData(generics.ListAPIView):
    serializer_class = LinkRegularDataSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        query_set = LinkRegularData.objects.filter(name=name).distinct()
        return query_set
"""

class RetrieveLink(APIView):
    def get(self, request, *args, **kwargs):
        name = self.kwargs['name']
        instance = RoomLink.objects.filter(name=name)
        instance.update(sought=True)

        response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': f'attachment; filename="{RoomLink.objects.get(name=name).display_name.lower()}.csv"'},
    )
        
        writer = csv.writer(response)
        writer.writerows(example_csv)
        instance.update(sought=False)
        return response

class GetRoomAPI(viewsets.ModelViewSet):
    serializer_class = RoomInfoSerializer

    def get_queryset(self):
        """Retrieve all Rooms owned by logged in user""" 

        queryset = Room.objects.all()
        serializer_class = RoomInfoSerializer
        query_set = queryset.filter(owner=self.request.user)
        return query_set

class GetAllRoomsView(viewsets.ModelViewSet):
    """Get all Rooms"""

    queryset = Room.objects.all()
    serializer_class = RoomInfoNoUsersSerializer

class GetRoomLinksByRoom(APIView):
    """Get Room Link by Room - used by Client"""
    serializer_class = RoomLinkSerializer

    def get(self, request, *args, **kwargs):
        queryset = RoomLink.objects.filter(room=self.kwargs['room']).distinct()
        serializer_class = RoomLinkSerializer
        arr = []
        for item in queryset:
            if item.users.filter(user=self.request.user.id).exists():
                if item.sought:
                    arr.append(item.display_name)
        return Response({"active_links": arr})