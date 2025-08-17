#This is your framework level response

import json

class HttpResponse:
    
    def __init__(self, headers = None, status = 200, body=''):
        if isinstance(status, int):
            self.status = status
        else:
            raise TypeError(f"status must be of type int, got {type(status).__name__}")
        if headers is None:
            self.header = {}
        else:
            self.header = headers
        self.body = body


class JsonResponse(HttpResponse):

    def __init__(self, headers = None, status = 200, data=''):
        if isinstance(status, int):
            status = status
        else:
            raise TypeError(f"status must be of type int, got {type(status).__name__}")
        if headers is None:
            headers = {'Content-Type' : 'application/json'}
        else:
            headers['Content-Type'] = 'application/json'
        
        if isinstance(data, dict):
            body = json.dumps(data)
        else:
            body = {}
        super().__init__(headers = headers, status = status, body = body)