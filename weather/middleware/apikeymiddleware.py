import os
from django.http import JsonResponse


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
        api_key = os.environ.get('API_KEY')
        if not api_key:
            return JsonResponse({'error': 'API key is not set'}, status=500)

        request.api_key = api_key

        response = self.get_response(request)
        return response
