
from datetime import datetime
from os import path


class RequestLoggingMiddleware:
    """
    Middleware to log the request method and path.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the request method and path
        user = request.user.username if request.user.is_authenticated else 'Anonymous'
        file_name = path.join(path.dirname(__file__), 'requests.log')
        # Log the request details to a file named 'requests.log'
        with open(file_name, 'a') as log_file:
            log_file.write(f"{datetime.now()} - User: {user} - Path: {request.path}\n")
        
        # Call the next middleware or view
        response = self.get_response(request)
        
        return response

class RestrictAccessByTimeMiddleware:
    """
    Middleware to restrict access to the site between 9PM and 6PM.
    check the current server time and deny access by returning an error 403 Forbidden

    if a user accesses the chat outside 9PM and 6PM.
    """
    def __init__(self, get_response):
        self.get_response = get_response

class RestrictAccessByTimeMiddleware:
    """
    Middleware to restrict access between 9 PM (21:00) and 6 PM (18:00).
    (Only allows access from 6 PM to 9 PM)
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        print(f"Current hour: {current_hour}")
        
        # Deny access if time is NOT between 6 PM (18) and 9 PM (21)
        if not (18 <= current_hour < 21):
            from django_restframework.views import HttpResponseForbidden
            return HttpResponseForbidden("Access is only allowed between 6 PM and 9 PM.")
        
        response = self.get_response(request)
        return response