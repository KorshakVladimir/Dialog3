"""
Django settings for csn project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g&x3e&dogige0=uuhl%3(%8nmmcy)v(1-o037smy+a5#67f$rt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cgm',
    'tree',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'cgm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_PATH, 'templates')],
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

WSGI_APPLICATION = 'cgm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases




# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'


# Add Shkuratovskiy A. {06.05.2015}

STATICFILES_DIRS = (os.path.join(PROJECT_PATH, 'static'),)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

ROOT_URLCONF = 'cgm.urls'

SESSION_SAVE_EVERY_REQUEST = True

MEDIA_URL = '/media/'
# Absolute path to the media directory
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
'USER': 'tj',
'PASSWORD': 'tj',
}
}

try:
   from . import local
except:
   DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'cgm_db',
                    'USER': 'cgm_usr',
                    'PASSWORD': '54321',
                    'HOST': '127.0.0.1',
                    'PORT': '3306',
                }
            }

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
#    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
#    ALLOWED_HOSTS = ['*']

# Static asset configuration

    # BASE_DIR = os.path.dirname(os.path.abspath(__file__)
STATIC_ROOT = 'staticfiles'
    # STATIC_URL = '/static/
STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
