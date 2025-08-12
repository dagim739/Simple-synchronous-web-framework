def app(environ, start_response):
    status = '200 OK'  # HTTP Status
    response_body = 'Hello, world! This is my first WSGI app.'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-length', str(len(response_body)))    
    ]
    start_response(status, response_headers)
    body = 'Hello, world! This is my first WSGI app.'
    return [body.encode('utf-8')]  # WSGI requires bytes