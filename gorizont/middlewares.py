import time


class StatsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_request(self, request):
        "Start time at request coming in"
        request.start_time = time.time()

    def process_response(self, request, response):
        "End of request, take time"
        total = time.time() - request.start_time

        # Add the header.
        response["X-total-time"] = int(total * 1000)
        return response
