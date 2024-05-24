import os


class ApiKeyMiddleware:
    def __init__(self, get_response):
        """
        Middleware constructor.

        Args:
            get_response (callable): The next middleware or the view callable.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Process incoming requests.

        Args:
            request (HttpRequest): The incoming HTTP request.

        Returns:
            HttpResponse: The HTTP response.
        """
        # Retrieve the API key from environment variables
        request.api_key = os.environ.get('API_KEY')

        response = self.get_response(request)
        return response
