"""
Django Middleware is a way to process requests and responses globally before and
after they reach the view layer. Middlewares are classes that process incoming HTTP requests
before they are passed to views and can modify responses before they are sent back to the
client. They are useful for implementing features like authentication, logging, or session
management.

To create custom middleware, you define a class with methods such as __init__, __call__,
process_request, or process_response.
"""

# Example of a custom Django middleware
class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to run before the view is called
        print("Before view processing")

        response = self.get_response(request)

        # add custom headers to the response
        response["X-Custom-Header"] = "Custom Value"

        # Code to run after the view is called
        print("After view processing")

        return response

# Middleware in Django is configured in the settings.py file using the MIDDLEWARE setting.
# You can add your custom middleware to the MIDDLEWARE list to apply it to all requests.
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'myapp.middleware.CustomMiddleware',  # Add your custom middleware here
# ]