import handlers


# Here is where you add your routes
url_patterns = [
#   ('/route', handler)
    ('/home', handlers.home),
    ('/contact', handlers.contact),
    ('/not-found', handlers.notfound)
]
