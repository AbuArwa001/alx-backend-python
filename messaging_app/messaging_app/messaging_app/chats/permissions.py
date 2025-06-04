from rest_framework import permissions


class IsChatParticipant(permissions.BasePermission):
    """
    Custom permission to only allow participants of a chat to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the chat from the view's kwargs
        chat = view.get_object()
        
        # Check if the user is a participant of the chat
        return request.user in chat.participants.all()
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is a participant of the chat
        return request.user in obj.participants.all()
class IsChatOwner(permissions.BasePermission):
    """
    Custom permission to only allow the owner of a chat to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the chat from the view's kwargs
        chat = view.get_object()
        
        # Check if the user is the owner of the chat
        return chat.owner == request.user
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is the owner of the chat
        return obj.owner == request.user
class IsSuperUser(permissions.BasePermission):
    """
    Custom permission to only allow superusers to access certain views.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and is a superuser
        return request.user.is_authenticated and request.user.is_superuser
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated and is a superuser
        return request.user.is_authenticated and request.user.is_superuser

class IsAdmin(permissions.BasePermission):
    """
    Custom permission to only allow admins of a chat to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the chat from the view's kwargs
        chat = view.get_object()
        
        # Check if the user is an admin of the chat
        return request.user in chat.admins.all()
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is an admin of the chat
        return request.user in obj.admins.all()
class IsConversationParticipant(permissions.BasePermission):
    """
    Custom permission to only allow participants of a conversation to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the conversation from the view's kwargs
        conversation = view.get_object()
        
        # Check if the user is a member of the conversation
        return request.user in conversation.participants.all()
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is a member of the conversation
        return request.user in obj.members.all()

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
