from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ConversationViewSet, MessageViewSet

urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('users/<uuid:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
    path('conversations/', ConversationViewSet.as_view({'get': 'list', 'post': 'create'}), name='conversation-list'),
    path('conversations/<uuid:pk>/', ConversationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='conversation-detail'),
    path('messages/', MessageViewSet.as_view({'get': 'list', 'post': 'create'}), name='message-list'),
    path('messages/<uuid:pk>/', MessageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='message-detail'),
]

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')
urlpatterns += [
    path('', include(router.urls)),
]
# This code defines the URL patterns for the messaging application, including routes for users, conversations, and messages.
# It uses Django's path and include functions to set up the URLs, and the DefaultRouter from Django REST Framework to automatically generate routes for the viewsets.
# The urlpatterns list includes paths for listing, creating, retrieving, updating, and deleting users, conversations, and messages.
# The UserViewSet, ConversationViewSet, and MessageViewSet are imported from the views module, which contains the logic for handling requests related to users, conversations, and messages.
# The code also includes a router that registers the viewsets, allowing for cleaner URL management and automatic generation of RESTful routes.
# 