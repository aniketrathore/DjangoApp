from Registration import serializer_module, models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_205_RESET_CONTENT, \
    HTTP_204_NO_CONTENT
from django.contrib.auth.hashers import make_password


class UserAPIView(APIView):
    serializer_class = serializer_module.UserModelSerializer

    def get(self, request):
        model = models.UserModel.objects.all()
        serializer_class = serializer_module.UserModelSerializer(model, many=True)
        return Response(serializer_class.data, HTTP_200_OK)

    def post(self, request):
        if request.method == "POST":
            user = serializer_module.UserModelSerializer(data=request.data)
            if user.is_valid():
                usr = user.save()
                usr.password = make_password(usr.password)
                usr.save()
                return Response(user.data, HTTP_201_CREATED)
        return Response(user.errors, HTTP_400_BAD_REQUEST)


class UserUpdate(APIView):
    serializer_class = serializer_module.UserModelSerializer

    def get_object(self, username):
        return models.UserModel.objects.get(username=username)

    def get(self, request, username, format=None):
        model = self.get_object(username)
        serializer = serializer_module.UserModelSerializer(model)
        return Response(serializer.data)

    def put(self, request, username, format=None):
        model = self.get_object(username=username)
        serializer = serializer_module.UserModelSerializer(model, data=request.data)
        if serializer.is_valid():
            usr = serializer.save()
            usr.password = make_password(usr.password)
            usr.save()
            return Response(serializer.data, HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

    def delete(self, request, username, format=None):
        model = self.get_object(username)
        model.delete()
        return Response(status=HTTP_204_NO_CONTENT)
