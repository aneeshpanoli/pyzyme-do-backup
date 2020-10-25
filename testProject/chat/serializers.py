from rest_framework import serializers
from chat.models import Message, UserName

# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    """For Serializing Message"""
    class Meta:
        model = Message
        fields = ['user', 'message', 'timestamp', 'stars']


class UserSerializer(serializers.ModelSerializer):
    """For Serializing user"""
    class Meta:
        model = UserName
        fields = ['uid', 'user']
