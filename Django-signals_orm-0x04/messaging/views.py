from django.shortcuts import render
from rest_framework import viewsets
from .models import Message, Notification, MessageHistory
from .serializers import MessageSerializer, NotificationSerializer, MessageHistorySerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from chats.models import User

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class MessageHistoryViewSet(viewsets.ModelViewSet):
    """
    Display the message edit history in the user interface, allowing users to view previous versions of their messages.
    """
    queryset = MessageHistory.objects.all()
    serializer_class = MessageHistorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

def delete_user(request, user_id):
    """
    Delete a user and all their messages, notifications, and message history.
    """
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return render(request, 'success.html', {'message': 'User and related data deleted successfully.'})
    except User.DoesNotExist:
        return render(request, 'error.html', {'message': 'User not found.'})
    except Exception as e:
        return render(request, 'error.html', {'message': str(e)})