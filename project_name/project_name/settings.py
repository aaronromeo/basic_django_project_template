"""
Django settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', '{{ secret_key }}')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.getenv('DEBUG', 0))

TEMPLATE_DEBUG = bool(os.getenv('DEBUG', 0))

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'south',
    # 'storages',

    # add magical apps here

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

DATABASES = {'default': dj_database_url.config(
        default="postgres://{}:{}@localhost/{}".format(os.getenv('DB_USER'), os.getenv('DB_PASS'), os.getenv('DB_NAME'))
        )}

# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/

STATIC_URL = '/static/'

STATIC_PATH = os.path.join(BASE_DIR, 'static/')
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static/')

STATICFILES_DIRS = (
            STATIC_PATH,
            )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_SECURE_URLS = False                                  # use http instead of https
AWS_QUERYSTRING_AUTH = False                                # don't add complex authentication-related query parameters for requests
AWS_S3_ACCESS_KEY_ID = os.getenv('AWS_S3_ACCESS_KEY_ID')    # enter your access key id
AWS_S3_SECRET_ACCESS_KEY = os.getenv('AWS_S3_SECRET_ACCESS_KEY')    # enter your secret access key
AWS_STORAGE_BUCKET_NAME = '{{ project_name }}'

