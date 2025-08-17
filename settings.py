# Here you add your middleware in the order of wrapping you want

MIDDLEWARESTACK = [
    'middlewares.middleware.LoggerMiddleware',
    'middlewares.middleware.TimeMiddleware',
]