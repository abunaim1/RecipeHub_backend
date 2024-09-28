from rest_framework import serializers
from .models import  Profile, ChatGroup, GroupMessage
from user.serializers import UserSerializers

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    class Meta:
        model = Profile
        fields = ['id', 'user', 'full_name', 'image']

class ChatGroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChatGroup
        fields = '__all__'

class GroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessage
        fields = '__all__'
