"""
Django settings for champagn project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.contrib import messages
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vofp&7z8i+d3dcf^-e0&bao2iizitpj3al5*c9i1t2azd#7cw^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
DJANGO_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth2_provider',
    'rest_framework',
    'corsheaders',
    'tinymce',
)

LOCAL_APPS = (
    'app',
    'master',
    'log',
    'job',
    'product',
    'frontendlogs',
    'cms',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'champagn.custom_middleware.LoggingMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'champagn.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

AUTH_USER_MODEL = 'app.User'

WSGI_APPLICATION = 'champagn.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'champagn_dev_local',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'EXCEPTION_HANDLER': 'champagn.exceptions.custom_exception_handler'
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

ADMIN_SITE_HEADER = 'FIZZ'

ADMIN_SITE_TITLE = 'FIZZ'

APPLICATION_NAME = 'CHAMPAGN_FIZZ'


CORS_ORIGIN_ALLOW_ALL = True

ADMIN_PAGE_SIZE = 20

LST_APP_FOR_LOGGING = ['app', 'master', 'product']

STATIC_URL = '/static/'

STATIC_ROOT = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static/v1/img/user_files/"),
)

MEDIA_ROOT = STATICFILES_DIRS[0]

# custom error codes
HTTP_USER_ERROR = 111

ADMIN_UNABELE_TO_LOGIN = 112

MESSAGE_KEY = 'message'

OAUTH2_PROVIDER = {
    'ACCESS_TOKEN_EXPIRE_SECONDS': 31546000,  # (seconds for one year)
}

OAUTH_EXPIRY_SECONDS = 31546000  # (seconds for one year)

# configuration for bootstrap
MESSAGE_TAGS = {
    messages.SUCCESS: 'alert-success success',
    messages.WARNING: 'alert-warning warning',
    messages.ERROR: 'alert-danger error'
}

# Email Settings
EMAIL_DEFAULT = 'VIP FIZZ < admin@vipfizz.com >'
EMAIL_USE_TLS = True
EMAIL_HOST = 'mail.netsolutionsindia.com'
EMAIL_HOST_USER = 'sugam.srivastava@netsolutionsindia.com'
EMAIL_HOST_PASSWORD = 'Sde8e4#%@1'
EMAIL_PORT = 25