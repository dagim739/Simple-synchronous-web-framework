# Here you define your middle wares

class LoggerMiddleware:
    def __init__(self, app):
        self.app = app
    def __call__(self, request, **kwargs):
        #do something on the request object
        response = self.app(request, **kwargs)
        #do something on the response object
        return response



class TimeMiddleware:
    def __init__(self, app):
        self.app = app
    def __call__(self, request, **kwargs):
        #do something on the request object
        response = self.app(request, **kwargs)
        #do something on the response object
        return response