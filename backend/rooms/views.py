from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from .models import RoomInfo
from .serializers import RoomInfoSerializer

class RoomApi(viewsets.ModelViewSet):
    queryset = RoomInfo.objects.all().order_by('name')
    lookup_field = 'name'
    serializer_class = RoomInfoSerializer

class Rooom(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        ser = RoomInfoSerializer(request.name)
        return Response(ser.data)