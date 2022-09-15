from .base import *

DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
STRIPE_PUBLIC_KEY = 'pk_live_51LdCIsLc7dX2nRon6GHUTaoSxnYjW21h6npty7YO5PaU54DghZScl6NhdvOP98DAO9Q5VQhNawNYPqOIikw5STcm00xMqNDkK5'
STRIPE_SECRET_KEY = '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'