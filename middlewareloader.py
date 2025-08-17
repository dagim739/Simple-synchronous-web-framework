# This loads the middleware in order

def middlewareloader(app, middlewarestack):
    for middleware_path in reversed(middlewarestack):
        module_name, class_name = middleware_path.rsplit('.', 1)
        module = __import__(module_name, fromlist=[class_name])
        middleware = getattr(module, class_name)
        app = middleware(app)
    return app