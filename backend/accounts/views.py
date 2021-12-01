from django.shortcuts import render
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions, viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from .serializers import UserSerializer, RegisterSerializer, ProfileSerializer
from .models import Profile
from django.contrib.auth.models import User

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginView(KnoxLoginView):
    #authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)

class LoginFromClientAPI(KnoxLoginView):
    """permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        temp_list=super(LoginFromClientAPI, self).post(request, format=None)
        if type(temp_list.data) is dict:
            username = request.data.get('username')
            return Response({"id": User.objects.filter(username=username).first().id})"""

class ProfileAPI(RetrieveAPIView):
    lookup_field = "user"
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        ser = UserSerializer(request.user)
        return Response(ser.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

class UserProfileAPI(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

"""
class UpdateProfile(generics.UpdateAPIView): # Update Profile Details
    serializer_class = ProfileSerializer

    def update(self, request,):
        instance = Profile.objects.filter(user=request.user)
        print(request.user)
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Success"})
        else:
            return Response({"message": "Error"})
"""