from cs_users.models import OUsers
from cs_users.serializers import OUserSerializers
from rest_framework import viewsets


class OUserViewSet(viewsets.ModelViewSet):
    queryset = OUsers.objects.all()
    serializer_class = OUserSerializers