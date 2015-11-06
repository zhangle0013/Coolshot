# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework.renderers import JSONRenderer
# from users.models import Users
# from users.serializers import UserSerializers
# # Create your views here.
#
#
# class JSONResponse(HttpResponse):
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(data, **kwargs)
#
#
# def user_list(request, num):
#     u = Users.objects.get(id=num)
#     ser = UserSerializers(u)
#     return JSONResponse(ser.data)

from users.models import Users
from users.serializers import UserSerializers
from rest_framework import APIView
from rest_framework import Response


class UserList(APIView):
    def get(self, request, format=None):
        users = Users.objects.all()
        ser = UserSerializers(users, many=True)
        return Response(ser.data)

    def post(self, request, format=None):
        ser = UserSerializers(request.DATA)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

class UserDetail(APIView):
    def get(self, request, num, format=None):
        u = Users.objects.get(id=num)
        ser = UserSerializers(u)
        return Response(ser.data)