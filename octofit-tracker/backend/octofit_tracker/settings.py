# ...existing code...
INSTALLED_APPS = [
    # ...existing code...
    'tracker',
    'rest_framework',
    'corsheaders',
    'dj_rest_auth',
    'django.contrib.sites',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ...existing code...
]

# Additional configurations
CORS_ALLOW_ALL_ORIGINS = True
SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}

ALLOWED_HOSTS = ['*']
# ...existing code...