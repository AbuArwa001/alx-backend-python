from django_filters import rest_framework as filters
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import User, Conversation, Message
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer


class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'username': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
            'date_joined': ['exact', 'gte', 'lte'],
        }

class ConversationFilter(filters.FilterSet):
    class Meta:
        model = Conversation
        fields = {
            'name': ['exact', 'icontains'],
            'created_at': ['exact', 'gte', 'lte'],
            'participants': ['exact'],
        }

class MessageFilter(filters.FilterSet):
    class Meta:
        model = Message
        fields = {
            'content': ['exact', 'icontains'],
            'timestamp': ['exact', 'gte', 'lte'],
            'sender': ['exact'],
            'conversation': ['exact'],
        }

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing users in the messaging application.
    Provides CRUD operations for User model.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = UserFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    def perform_destroy(self, instance):
        """
        Delete the user instance.
        """
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def list(self, request, *args, **kwargs):
        """
        List all users in the messaging application.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a specific user by ID.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    def get_permissions(self):
        """
        Get the permissions for the UserViewSet.
        """
        if self.action in ['create', 'update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
    def get_serializer_class(self):
        """
        Get the serializer class for the UserViewSet.
        """
        if self.action in ['create', 'update']:
            return UserSerializer
        return UserSerializer
class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing conversations in the messaging application.
    Provides CRUD operations for Conversation model.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ConversationFilter

    def get_queryset(self):
        """
        Override the default queryset to filter conversations based on the authenticated user.
        """
        user = self.request.user
        if user.is_authenticated:
            return Conversation.objects.filter(participants=user)
        return Conversation.objects.none()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        conversation = serializer.save()
        return Response(ConversationSerializer(conversation).data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        conversation = serializer.save()
        return Response(ConversationSerializer(conversation).data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        """
        Delete the conversation instance.
        """
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        """
        List all conversations in the messaging application.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a specific conversation by ID.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_permissions(self):
        """
        Get the permissions for the ConversationViewSet.
        """
        if self.action in ['create', 'update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_serializer_class(self):
        """
        Get the serializer class for the ConversationViewSet.
        """
        if self.action in ['create', 'update']:
            return ConversationSerializer
        return ConversationSerializer
class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing messages in the messaging application.
    Provides CRUD operations for Message model.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = MessageFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        message = serializer.save()
        return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        message = serializer.save()
        return Response(MessageSerializer(message).data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        """
        Delete the message instance.
        """
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        """
        List all messages in the messaging application.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a specific message by ID.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_permissions(self):
        """
        Get the permissions for the MessageViewSet.
        """
        if self.action in ['create', 'update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_serializer_class(self):
        """
        Get the serializer class for the MessageViewSet.
        """
        if self.action in ['create', 'update']:
            return MessageSerializer
        return MessageSerializer


