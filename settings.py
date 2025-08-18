# Here you add your middleware in the order of wrapping you want

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

# Define the maximum file size your app will return once in bytes
# This depends on depends on the balance between performance and memory usage
# tt is ok to up to 50MB or 50000000bytes if your server has the memory capacity
# but the default value is the preferred one.
MAX_BYTE_SIZE = 2000000

# Define the maximum chunk size your app will return in bytes
MAX_CHUNK_SIZE = 8000

# Here you add your middleware in the order of wrapping you want
MIDDLEWARESTACK = [
    'middlewares.middleware.LoggerMiddleware',
    'middlewares.middleware.TimeMiddleware',
]


# define database address and the ORM engine
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'drdebeletola',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': 'root',
    }
}


# the url to check if the client is looking for static files
STATIC_URL = '/static'

# Path to where you put static files
STATICFILES_DIRS = [
    BASE_DIR / "static"
]


FAVICON_URL = "/favicon.ico"


FAVICON_DIR = BASE_DIR / "static" / "favicon"