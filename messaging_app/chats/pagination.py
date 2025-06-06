
from rest_framework.pagination import PageNumberPagination

class MessagePagination(PageNumberPagination):
    """
    Custom pagination class for messages in conversations.
    """
    page_size = 20  # Default number of messages per page
    page_size_query_param = 'page_size'  # Allow clients to set page size
    max_page_size = 100  # Maximum allowed page size to prevent abuse
    last_page_strings = ('last',)  # Allow 'last' as a string to get the last page
    first_page_string = 'first'  # Allow 'first' as a string to get the first page
