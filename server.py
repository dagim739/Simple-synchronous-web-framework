from wsgiref.simple_server import make_server
from app import app

if __name__ == '__main__':
    server = make_server('localhost', 8000, app)
    print("Serving on http://localhost:8000")
    server.serve_forever()
