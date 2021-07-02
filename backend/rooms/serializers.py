from rest_framework import serializers
from .models import RoomInfo

class RoomInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoomInfo
        fields = ['id', 'name', 'dev_name', 'brief_desc']
        extra_kwargs = {'url': {'lookup_url': 'name'}}