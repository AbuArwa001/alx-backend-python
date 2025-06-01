from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, ConversationViewSet, MessageViewSet

urlpatterns = []
# This file defines the URL patterns for the messaging application.
# It includes routes for user management, conversation handling, and message operations.
# The urlpatterns list is initialized as empty and will be populated with paths for the API endpoints.
# Import necessary modules and viewsets for routing
router = routers.DefaultRouter()
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