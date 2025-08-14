import re


class RouteNotFound(Exception):
    pass



class Dispatcher:

    def __init__(self):
        self.routes = []


    def add(self, path_pattern, handler):
        # Convert dynamic segments like <id> to regex groups
        pattern = re.sub(r'<(\w+)>', r'(?P<\1>[^/]+)', path_pattern)
        pattern = f"^{pattern}$"
        compiled = re.compile(pattern)
        self.routes.append((compiled, handler))


    def match(self, path):
        for pattern, handler in self.routes:
            match = pattern.match(path)
            if match:
                return handler, match.groupdict()
        raise RouteNotFound(f"No route matches {path}")