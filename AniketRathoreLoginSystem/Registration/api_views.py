from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from .serealizer import ShowUserDataSerializer, RegisterNewUserSerializer, UserUpdateViewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserDataShowAPI(APIView):
    def get(self, request, format=None):
        model = User.objects.all()
        serializer = ShowUserDataSerializer(model, many=True)
        return Response(serializer.data)


class RegisterNewUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterNewUserSerializer


class UserDataAll(APIView):
    serializer_class = UserUpdateViewSerializer

    def get_object(self, username):
        return User.objects.get(username=username)

    def get(self, request, username, format=None):
        model = self.get_object(username)
        serializer = RegisterNewUserSerializer(model)
        return Response(serializer.data)

    def put(self, username, request, *args, **kwargs):
        data = request.data

        serializer = UserUpdateViewSerializer(data=data)
        if serializer.is_valid():
            data = serializer.data
            serializer.save()
            return Response(data, status.HTTP_200_OK)

    def delete(self, request, username, format=None):
        model = self.get_object(username)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateUserPassword(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateViewSerializer
    lookup_field = 'username'
