from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class User(models.Model, AbstractBaseUser):
    """
    Custom user model for the messaging application.
    This model extends Django's AbstractBaseUser to provide a custom user
    model with fields for username, email, and password.
    """
    class UserManager(BaseUserManager):
        def create_user(self, username, email, password=None):
            if not email:
                raise ValueError("Users must have an email address")
            if not username:
                raise ValueError("Users must have a username")
            user = self.model(
                username=username,
                email=self.normalize_email(email),
            )
            user.set_password(password)
            user.save(using=self._db)
            return user

        def create_superuser(self, username, email, password=None):
            user = self.create_user(username, email, password)
            user.is_staff = True
            user.is_superuser = True
            user.save(using=self._db)
            return user
    objects = UserManager()
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def __str__(self):
        return self.username


class Conversation(models.Model):
    """
    Model representing a conversation between users.
    Each conversation can have multiple participants.
    """
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id} with {self.participants.count()} participants"

class Message(models.Model):
    """
    Model representing a message in a conversation.
    Each message is linked to a specific conversation and user.
    """
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.id} from {self.sender.username} in Conversation {self.conversation.id}"
 