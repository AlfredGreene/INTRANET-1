import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

SECRET_KEY = config('INTRA_SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []


# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'local_apps.brands',
    'local_apps.dashboard',
    'local_apps.frontend',
    'local_apps.inventory',
    'local_apps.organization',
    'local_apps.profiles',
    'local_apps.reports',
    'local_apps.resume',
    'local_apps.tickets',
]

THIRD_PARTY_APPS = []

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'intra.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir),'templates')),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'intra.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS':{
            'min_length': 9,
        },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

"""   Extra Conf.          """
LANGUAGE_CODE = 'es-us'
TIME_ZONE = 'America/Panama'
USE_I18N = True
USE_L10N = True
USE_TZ = False
FIRST_DAY_OF_WEEK = 1

""" Storages Conf           """
DEFAULT_FILE_STORAGE = 'storages.backends.ftp.FTPStorage'
FTP_STORAGE_LOCATION = config("INTRA_FTP_STORAGE_LOCATION",)

""" Email Conf.             """
EMAIL_HOST = config("INTRA_EMAIL_HOST",)
EMAIL_PORT = config("INTRA_EMAIL_PORT", cast=int)
EMAIL_HOST_USER = config("INTRA_EMAIL_HOST_USER",)
EMAIL_HOST_PASSWORD = config("INTRA_EMAIL_HOST_PASSWORD",)
EMAIL_USE_TLS = config("INTRA_EMAIL_USE_TLS", cast=bool)

""" Security Conf           """
# AUTH_USER_MODEL = 'local_apps.intra_profile.User'
AUTHENTICATION_BACKENDS =(
                            'django.contrib.auth.backends.ModelBackend',
                            'local_apps.profiles.EmailBackend.EmailBackend',
                        )
LOGIN_URL = '/entrar/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'http://phoenixworldtrade.com/'
SESSION_COOKIE_AGE = 43200
SESSION_COOKIE_NAME = 'session'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

""" Media Configuration     """
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir),'media'))

""" Static Files Conf       """
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir),'staticfiles')),
)
