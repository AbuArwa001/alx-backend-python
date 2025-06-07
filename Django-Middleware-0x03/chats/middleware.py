
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
        print(f"file name: {file_name}")
        with open(file_name, 'a') as log_file:
            log_file.write(f"{datetime.now()} - User: {user} - Path: {request.path}\n")
        
        # Call the next middleware or view
        response = self.get_response(request)
        
        return response