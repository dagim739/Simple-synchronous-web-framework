import re
import handlers

from routes import url_patterns

class RouteNotFound(Exception):
    pass

class Dispatcher:

    def __init__(self):
        self.routes = []


    def add(self, url_patterns):
        if len(url_patterns) > 0:
            for pattern, handler in url_patterns:
                pattern = re.sub(r'<(\w+)>', r'(?P<\1>[^/]+)', pattern)
                pattern = f"^{pattern}$"
                compiled = re.compile(pattern)
                self.routes.append((compiled, handler))



    def match(self, path):
        for pattern, handler in self.routes:
            match = pattern.match(path)
            if match:
                return handler, match.groupdict()

        return handlers.notfound, {}
        # raise RouteNotFound(f"No route matches {path}")

dispatcher = Dispatcher()

dispatcher.add(url_patterns)
