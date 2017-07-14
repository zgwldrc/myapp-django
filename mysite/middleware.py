from django.http import HttpResponse


class CorsMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.method == 'OPTIONS':
            response = HttpResponse()
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Methods'] = 'PUT,POST,DELETE'
            response['Access-Control-Allow-Headers'] = 'Content-Type'
            response['Access-Control-Max-Age'] = 86400
            return response

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        response['Access-Control-Allow-Origin'] = '*'

        return response


