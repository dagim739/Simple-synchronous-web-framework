class Response:

    def __init__(self, status = 200, body = '', headers = None):
        try:
            int(status)
            if (status < 100 or status > 599):
                raise ValueError("status code must be between 100 and 599")
            else:
                self.status = status
        except TypeError:
            raise TypeError(f"status must be type int, got {type(status).__name__}")
        if headers is None:
            self.headers = {}
        else:
            self.headers = headers
        if isinstance(body, bytes):
            self.body = body
        elif isinstance(body, str):
            self.body = body.encode('utf-8')
        else:
            raise TypeError(f"headers must be of type str or bytes, got {type(headers).__name__}")
        
    def __call__(self, start_response):
        status_str = f"{self.status} {_status_text(self.status)}"
        headers_list = [('Content-Type', 'text/html; charset=utf-8')] + list(self.headers.items())
        start_response(status_str, headers_list)
        return [self.body]
        

    def _status_text(status_code):
        http_status_codes = {
            100: "Continue",
            101: "Switching Protocols",
            102: "Processing",
            103: "Early Hints",

            200: "OK",
            201: "Created",
            202: "Accepted",
            203: "Non-Authoritative Information",
            204: "No Content",
            205: "Reset Content",
            206: "Partial Content",
            207: "Multi-Status",
            208: "Already Reported",
            226: "IM Used",

            300: "Multiple Choices",
            301: "Moved Permanently",
            302: "Found",
            303: "See Other",
            304: "Not Modified",
            305: "Use Proxy",
            307: "Temporary Redirect",
            308: "Permanent Redirect",

            400: "Bad Request",
            401: "Unauthorized",
            402: "Payment Required",
            403: "Forbidden",
            404: "Not Found",
            405: "Method Not Allowed",
            406: "Not Acceptable",
            407: "Proxy Authentication Required",
            408: "Request Timeout",
            409: "Conflict",
            410: "Gone",
            411: "Length Required",
            412: "Precondition Failed",
            413: "Payload Too Large",
            414: "URI Too Long",
            415: "Unsupported Media Type",
            416: "Range Not Satisfiable",
            417: "Expectation Failed",
            418: "I'm a teapot",
            421: "Misdirected Request",
            422: "Unprocessable Entity",
            423: "Locked",
            424: "Failed Dependency",
            425: "Too Early",
            426: "Upgrade Required",
            428: "Precondition Required",
            429: "Too Many Requests",
            431: "Request Header Fields Too Large",
            451: "Unavailable For Legal Reasons",

            500: "Internal Server Error",
            501: "Not Implemented",
            502: "Bad Gateway",
            503: "Service Unavailable",
            504: "Gateway Timeout",
            505: "HTTP Version Not Supported",
            506: "Variant Also Negotiates",
            507: "Insufficient Storage",
            508: "Loop Detected",
            510: "Not Extended",
            511: "Network Authentication Required"
        }
        return http_status_codes.get(status_code, 'None standard status codes are not supported')
