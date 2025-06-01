from .models import User, Conversation, Message
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    """
    Serializer for the User model.
    Converts User instances to and from JSON format.
    """
    user_id = serializers.UUIDField(read_only=True)
    username = serializers.CharField(max_length=150, required=True, allow_blank=False)
    email = serializers.EmailField(max_length=255, required=True, allow_blank=False)
    first_name = serializers.CharField(max_length=150, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=150, required=False, allow_blank=True)
    phone_number = serializers.CharField(max_length=15, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'first_name', 'last_name', 'phone_number']
        read_only_fields = ['user_id']



class MessageSerializer(serializers.Serializer):
    """
    Serializer for the Message model.
    Converts Message instances to and from JSON format.
    """

    message_id = serializers.UUIDField(read_only=True)
    message_body = serializers.CharField(required=True, allow_blank=False)
    sent_at = serializers.DateTimeField(read_only=True)
    sender = UserSerializer(read_only=True)


    def validate_message_body(self, value):
        """
        Validate that the message body is not empty.
        """
        if not value.strip():
            raise serializers.ValidationError("Message body cannot be empty.")
        return value
    class Meta:
        model = Message
        fields = ['message_id', 'message_body', 'sent_at', 'conversation', 'sender']
        read_only_fields = ['message_id', 'sent_at']
    
    
class ConversationSerializer(serializers.Serializer):
    """
    Serializer for the Chat model.
    Converts Chat instances to and from JSON format.
    """
    messages = MessageSerializer(many=True, read_only=True)
    conversation_id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255, required=False, allow_blank=True)
    participants = UserSerializer(many=True, read_only=True)
    total_messages = serializers.SerializerMethodField()
    def get_total_messages(self, obj):
        """
        Return the total number of messages in the conversation.
        """
        return obj.messages.count()
    
    class Meta:
        model = Conversation
        fields = ['conversation_id', 'name', 'participants']
        read_only_fields = ['conversation_id']
        extra_kwargs = {
            'name': {'required': False, 'allow_blank': True},
            'participants': {'read_only': True}
        }
        depth = 1
    def validate_name(self, value):
        """
        Validate that the conversation name is not empty.
        """
        if not value.strip():
            raise serializers.ValidationError("Conversation name cannot be empty.")
        return value
    def validate_participants(self, value):
        """
        Validate that at least one participant is provided.
        """
        if not value:
            raise serializers.ValidationError("At least one participant is required.")
        return value
        