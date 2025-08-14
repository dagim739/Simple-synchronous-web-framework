from request import Request

from response import Response

from dispatcher import dispatcher

def app(environ, start_response):
    request = Request(environ)
    status = 200  # HTTP Status
    handler, kwargs = dispatcher.match(request.path)
    print (kwargs)
    print (type(kwargs))
    response_body = handler(request, **kwargs)
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-length', str(len(response_body)))    
    ]
    response = Response(status = status, body = response_body, headers = response_headers)
    return response(start_response)