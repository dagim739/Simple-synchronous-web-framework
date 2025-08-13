from request import Request

from response import Response


def app(environ, start_response):
    request = Request(environ)
    status = 200  # HTTP Status
    response_body = 'Hello, world! This is my first WSGI app.'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-length', str(len(response_body)))    
    ]
    response = Response(status = status, body = response_body, headers = response_headers)
    return response(start_response)