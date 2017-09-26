"""
Django settings for startup project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v=$3izfrb71c^h0!8iy1-*#h9szf8tlja$q&-vf-hfr%9-h1q*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['django-env.4npgimxieq.ap-south-1.elasticbeanstalk.com','www.bookfish.in', '127.0.0.1', 'bookfish.au-syd.mybluemix.net']

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'dewanshupartihar@gmail.com'
# EMAIL_HOST_PASSWORD = 'walterwhite318'
# EMAIL_USE_TLS = True

# EMAIL_HOST = 'smtp.elasticemail.com'
# EMAIL_PORT = 2525
# EMAIL_HOST_USER = 'dewanshu.pratihar@gmail.com'
# EMAIL_HOST_PASSWORD = '6d7db482-3039-4be2-871f-e8efe52c1542'
# EMAIL_USE_TLS = True

EMAIL_HOST = 'email-smtp.eu-west-1.amazonaws.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'AKIAIYFBJU5YNJ65KF5Q'
EMAIL_HOST_PASSWORD = 'AggFua6WdOsshhqi+bK7Mhf7VeHPlqHcxXVC0BFziUSB'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Bookfish Team <no-reply@bookfish.in>'

SOCIAL_AUTH_FACEBOOK_KEY = '750409465124304'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '8b1277fe15ba3c1c13a5eab14e24d894'  # App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'fb'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #my_apps
    'bookswap',

    #3rd party
    'crispy_forms',
    'social_django',
    #'social.apps.django_app.default',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #3rd party
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/plus.login'
]

ROOT_URLCONF = 'startup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                #3rd party
                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect', # <--
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

# SOCIAL_AUTH_PIPELINE = (
#     'social.pipeline.user.user_details'
# )

WSGI_APPLICATION = 'startup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# if 'RDS_DB_NAME' in os.environ:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': os.environ['RDS_DB_NAME'],
#             'USER': os.environ['RDS_USERNAME'],
#             'PASSWORD': os.environ['RDS_PASSWORD'],
#             'HOST': os.environ['RDS_HOSTNAME'],
#             'PORT': os.environ['RDS_PORT'],
#         }
#     }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', 
#         'NAME': 'bmix-syd-yp-3fd9b1db-8bad-4cb6-82b5-2cad0f47cad4',
#         'USER': 'admin',
#         'PASSWORD': 'RKVDZOMGEIPTFENN',
#         'HOST': 'sl-aus-syd-1-portal.3.dblayer.com',   # Or an IP Address that your DB is hosted on
#         'PORT': '17539',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'ebdb',
        'USER': 'root',
        'PASSWORD': 'bookfish446',
        'HOST': 'aadqgn9k15s9kh.cwf3btudsw9r.ap-south-1.rds.amazonaws.com',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': '',                      # Or path to database file if using sqlite3.
#         'USER': '',                      # Not used with sqlite3.
#         'PASSWORD': '',                  # Not used with sqlite3.
#         'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#     }
# }

# import dj_database_url
# DATABASES['default'] = dj_database_url.config()

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


STATIC_URL = '/www/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "www", "static")

STATICFILES_DIRS = ( 
    os.path.join(BASE_DIR, "static"),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "media_root")

CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_CLASS_CONVERTERS = {'textinput': "textinput loginInp"}