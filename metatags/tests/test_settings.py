SECRET_KEY = 'test_key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'metatags'
]
