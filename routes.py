import views


# Here is where you add your routes
url_patterns = [
#   ('/route', handler)
    ('/home', views.home),
    ('/contact', views.contact),
    ('/about', views.about),
    ('/services', views.services),
]