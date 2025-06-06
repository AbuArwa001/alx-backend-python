from rest_framework import permissions

from .models import Conversation
# Import typing for type annotations to enhance code clarity
from typing import Optional
from rest_framework.request import Request
from rest_framework.views import View

# class IsChatParticipant(permissions.BasePermission):
#     """
#     Custom permission to only allow participants of a chat to access it.
#     """

#     def has_permission(self, request, view):
#         # Check if the user is authenticated
#         if not request.user.is_authenticated:
#             return False
        
#         # Get the chat from the view's kwargs
#         chat = view.get_object()
        
#         # Check if the user is a participant of the chat
#         return request.user in chat.participants.all()
#     def has_object_permission(self, request, view, obj):
#         # Check if the user is authenticated
#         if not request.user.is_authenticated:
#             return False
        
#         # Check if the user is a participant of the chat
#         return request.user in obj.participants.all()
# class IsChatOwner(permissions.BasePermission):
#     """
#     Custom permission to only allow the owner of a chat to access it.
#     """

#     def has_permission(self, request, view):
#         # Check if the user is authenticated
#         if not request.user.is_authenticated:
#             return False
        
#         # Get the chat from the view's kwargs
#         chat = view.get_object()
        
#         # Check if the user is the owner of the chat
#         return chat.owner == request.user
#     def has_object_permission(self, request, view, obj):
#         # Check if the user is authenticated
#         if not request.user.is_authenticated:
#             return False
        
#         # Check if the user is the owner of the chat
#         return obj.owner == request.user
# class IsSuperUser(permissions.BasePermission):
#     """
#     Custom permission to only allow superusers to access certain views.
#     """

#     def has_permission(self, request, view):
#         # Check if the user is authenticated and is a superuser
#         return request.user.is_authenticated and request.user.is_superuser
    
#     def has_object_permission(self, request, view, obj):
#         # Check if the user is authenticated and is a superuser
#         return request.user.is_authenticated and request.user.is_superuser

# class IsAdmin(permissions.BasePermission):
#     """
#     Custom permission to only allow admins of a chat to access it.
#     """

#     def has_permission(self, request, view):
#         # Check if the user is authenticated
#         if not request.user.is_authenticated:
#             return False
        
#         # Get the chat from the view's kwargs
#         chat = view.get_object()
        
#         # Check if the user is an admin of the chat
#         return request.user in chat.admins.all()
    
#     def has_object_permission(self, request, view, obj):
#         # Check if the user is authenticated
#         if not request.user.is_authenticated:
#             return False
        
#         # Check if the user is an admin of the chat
#         return request.user in obj.admins.all()
class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to only allow participants of a conversation to access it.
    """
    
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
            
        # For list/create actions, check if they're trying to access a conversation they're in
        if view.action in ['list', 'create']:
            # For nested messages creation
            if 'conversation_pk' in view.kwargs:
                conversation_id = view.kwargs['conversation_pk']
                return Conversation.objects.filter(
                    conversation_id=conversation_id,
                    participants=request.user
                ).exists()
            return True  # Allow listing messages with filters
            
        # For other actions, rely on has_object_permission
        return True

    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
            
        # For conversation objects
        if isinstance(obj, Conversation):
            return obj.participants.filter(id=request.user.id).exists()
            
        # For message objects
        if hasattr(obj, 'conversation'):
            return obj.conversation.participants.filter(id=request.user.id).exists()
            
        return False
class IsChatMember(permissions.BasePermission):
    """
    Custom permission to only allow members of a chat to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the chat from the view's kwargs
        chat = view.get_object()
        
        # Check if the user is a member of the chat
        return request.user in chat.members.all()
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is a member of the chat
        return request.user in obj.members.all()

class IsMessageSender(permissions.BasePermission):
    """
    Custom permission to only allow the sender of a message to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the message from the view's kwargs
        message = view.get_object()
        
        # Check if the user is the sender of the message
        return message.sender == request.user
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is the sender of the message
        return obj.sender == request.user
