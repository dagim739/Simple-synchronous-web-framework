import os
import mimetypes
import settings
from app import app

def StaticFileMiddleware(environ, start_response):
    path_info = environ.get('PATH_INFO', '')
    if (path_info.startswith(settings.FAVICON_URL)):
        file_path = os.path.join(settings.FAVICON_DIR, path_info[1:])
        print (file_path)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            content_type, _ = mimetypes.guess_type(file_path)
            if content_type is None:
                content_type = "application/octet_stream"
            with open(file_path, 'rb') as f:
                filesize = os.path.getsize(file_path)
                if filesize > settings.MAX_BYTE_SIZE:
                    # you must read about iterators and generators to do this.
                    pass
                else:
                    body = f.read()
                status = "200 OK"
                response_headers = [
                    ('Content-Length', str(len(body))),
                    ('Content-Type', content_type),
                    ('X-Processed-By', 'WSGI_middleware_SFM')
                ]
                start_response(status, response_headers)
                return [body]
        else:
            status = "404 Not found"
            response = b''
            response_headers = [
                ('Content-Length', str(len(response))),
                ('X-Processed-By', 'WSGI_middleware_SFM')
            ]
            start_response(status, response_headers)
            return [response]
    
    elif (path_info.startswith(settings.STATIC_URL)):
        for staticfiledir in settings.STATICFILES_DIRS:
            file_path = os.path.join(staticfiledir,path_info[len(settings.STATIC_URL) + 1:])
            if os.path.exists(file_path) and os.path.isfile(file_path):
                content_type, _ = mimetypes.guess_type(file_path)
                if content_type is None:
                    content_type = "application/octet-stream"
                with open(file_path, 'rb') as f:
                    file_size = os.path.getsize(file_path)
                    if file_size > int(settings.MAX_BYTE_SIZE):
                        # you must read about iterators and generators to do this.
                        pass
                    else:
                        body = f.read()
                        status = '200 OK'
                        response_headers = [
                            ('Content-Length', str(len(body))),
                            ('Content-Type', content_type),
                            ('X-Processed-By', 'WSGI_middleware_SFM')
                        ]
                        start_response(status, response_headers)
                        return [body]
        status = "404 Not found"
        response = b''
        response_headers = [
            ('Content-Length', str(len(response))),
            ('X-Processed-By', 'WSGI_middleware_SFM')
        ]
        start_response(status, response_headers)
        return [response]
    else:
        return app(environ, start_response)