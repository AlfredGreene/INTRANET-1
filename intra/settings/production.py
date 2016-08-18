from intra.settings.base import *


SECRET_KEY = config('INTRA_SECRET_KEY')

DEBUG = config('INTRA_DEBUG',default=False, cast=bool)

ALLOWED_HOSTS = ['intra.phoenixworldtrade.com']

# AUTH_USER_MODEL = 'intra_profile.User'

DATABASES ={
            'default':{
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': config('INTRA_DB_NAME'),
                'USER': config('INTRA_DB_USER'),
                'PASSWORD': config('INTRA_DB_PASSWORD'),
                'HOST': config('INTRA_DB_HOST'),
                'PORT': config('INTRA_DB_PORT',cast=int),
                }
            }
