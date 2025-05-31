from serializers import ModelSerializer
from .models import User, Conversation, Message
from rest_framework import serializers


class UserSerializer(ModelSerializer):
    """
    Serializer for the User model.
    Converts User instances to and from JSON format.
    """
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'first_name', 'last_name', 'phone_number']
        read_only_fields = ['user_id']
        extra_kwargs = {
            'username': {'required': True, 'allow_blank': False},
            'email': {'required': True, 'allow_blank': False}
        }
    def create(self, validated_data):
        """
        Create a new User instance with the provided validated data.
        """
        user = User.objects.create_user(**validated_data)
        return user
class MessageSerializer(ModelSerializer):
    """
    Serializer for the Message model.
    Converts Message instances to and from JSON format.
    """
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'message_body', 'sent_at', 'conversation', 'sender']
        read_only_fields = ['message_id', 'sent_at', 'sender']
        extra_kwargs = {
            'message_body': {'required': True, 'allow_blank': False},
            'conversation': {'required': True}
        }
    def create(self, validated_data):
        """
        Create a new Message instance with the provided validated data.
        """
        message = Message.objects.create(**validated_data)
        return message
    

class ConversationSerializer(ModelSerializer):
    """
    Serializer for the Chat model.
    Converts Chat instances to and from JSON format.
    """
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'name', 'participants', 'created_at']
        read_only_fields = ['conversation_id', 'created_at']
        extra_kwargs = {
            'name': {'required': False, 'allow_blank': True}
        }
    def create(self, validated_data):
        """
        Create a new Chat instance with the provided validated data.
        """
        ConVo = Conversation.objects.create(**validated_data)
        return ConVo
    def update(self, instance, validated_data):
        """
        Update an existing Chat instance with the provided validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

