from wsgiref.simple_server import make_server
from wsgimiddleware import StaticFileMiddleware

if __name__ == '__main__':
    server = make_server('localhost', 8000, StaticFileMiddleware)
    print("Serving on http://localhost:8000")
    server.serve_forever()
