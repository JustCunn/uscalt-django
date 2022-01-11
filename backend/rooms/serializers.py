from rest_framework import serializers
from .models import Room, RoomLink, MainSilo, AuxSilo #LinkRegularData

class RoomLinkSerializer(serializers.ModelSerializer):
    
    is_bought_by_me = serializers.SerializerMethodField('_bought')
    user_count = serializers.SerializerMethodField('_count')

    def _bought(self, obj):
        uid = self.context.get('uid')

        return obj.buyers.filter(id=uid).count() > 0

    def _count(self, obj):
        if obj.off_id is None:
            return AuxSilo.objects.filter(link=obj.name).count()
        else:
            return False


    class Meta: 
        model = RoomLink

        fields = ['id', 'display_name', 'desc', 'room', 
                'name', 'sought', 'call_time', 'fields', 'is_bought_by_me', 'user_count']
        extra_kwargs = {'url': {'lookup_url': 'id'}}

class RoomLinkOwnerSerializer(serializers.ModelSerializer):

    class Meta: 
        model = RoomLink

        fields = ['id', 'display_name', 'desc', 'room', 'users', 'buyers', 
                'name', 'sought', 'call_time', 'fields',]
        extra_kwargs = {'url': {'lookup_url': 'id'}}

class RoomInfoSerializer(serializers.ModelSerializer):
    links = RoomLinkOwnerSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'name', 'dev_name', 'brief_desc', 'owner', 'links']
        extra_kwargs = {'url': {'lookup_url': 'name'}}

class RoomInfoNoUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'dev_name', 'brief_desc', 'owner',]
        extra_kwargs = {'url': {'lookup_url': 'name'}}


class MainSiloSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSilo
        fields = ['id', 'name', 'data']
        extra_kwargs = {'url': {'lookup_url': 'name'}}

class AuxSiloSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuxSilo
        fields = ['id', 'name', 'data', 'link', 'time']

class RegisterRoom(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name', 'dev_name', 'brief_desc', 'owner')
        extra_kwargs = {'owner': {'read_only': True}}

"""
class LinkRegularDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkRegularData
        fields = ('name', 'data')
        #extra_kwargs = {'url': {'lookup_url': 'name'}}
"""