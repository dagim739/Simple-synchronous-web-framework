from request import Request

from response import Response

from dispatcher import dispatcher

from middlewareloader import middlewareloader

from settings import MIDDLEWARESTACK

def app(environ, start_response):
    request = Request(environ)
    handler, kwargs = dispatcher.match(request.path)
    stacked = middlewareloader(handler, MIDDLEWARESTACK)
    handler_response = stacked(request, **kwargs)
    status = handler_response.status
    response_headers = [
        ('Content-Length', str(len(handler_response.body)))    
    ]
    response_headers = response_headers + list(handler_response.header.items())
    response = Response(status = status, body = handler_response.body, headers = response_headers)
    return response(start_response)