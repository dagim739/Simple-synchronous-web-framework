from urllib.parse import parse_qs


class Request:

    def __init__(self, environ):
        self.environ = environ
        self.method = environ['REQUEST_METHOD']
        self.path = environ['PATH_INFO']
        self.query_string = environ.get('QUERY_STRING', '')
        self.GET = parse_qs(self.query_string)
        try:
            content_length = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError, TypeError):
            content_length = 0
        self.body = ''
        if (content_length > 0):
            self.body = environ['wsgi.input'].read(content_length)
        else:
            pass
        self.POST = {}
        if self.method == 'POST':
            if "application/x-www-form-urlencoded" in environ['CONTENT_TYPE']:
                self.POST = parse_qs(self.body.decode())
            else:
                pass
            
    @property
    def headers(self):
        headers = {}
        for key, value in self.environ.items():
            if (key.startswith('HTTP_')):
                headers.update({key[5:].replace('_', '-').title() : value})
            else:
                continue
        return headers