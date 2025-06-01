from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# class User(models.Model, AbstractBaseUser):
class User(AbstractBaseUser):
    """
    Custom user model for the messaging application.
    This model extends Django's AbstractBaseUser to provide a custom user
    model with fields for username, email, and password.
    """
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    last_name = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.username


class Conversation(models.Model):
    """
    Model representing a conversation between users.
    Each conversation can have multiple participants.
    """
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    # Many-to-many relationship with User model to allow multiple participants
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id} with {self.participants.count()} participants"

class Message(models.Model):
    """
    Model representing a message in a conversation.
    Each message is linked to a specific conversation and user.
    """
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    # Foreign key to link message to a conversation and sender
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='conversations')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')

    def __str__(self):
        return f"Message {self.id} from {self.sender.username} in Conversation {self.conversation.id}"
 