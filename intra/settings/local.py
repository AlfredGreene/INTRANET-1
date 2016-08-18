from intra.settings.base import *

STATICFILES_DIRS = ('',)

STATIC_ROOT = os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir),'staticfiles'))

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
