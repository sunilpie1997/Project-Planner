
import os
from pathlib import Path
from . import google_conf


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^*y8cki98_xa%jf_kwbb1r+wxako74xpdlwp&1!^3k2=@%ybz4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#instead add 'CORS_ORIGIN_WHITELIST'
CORS_ORIGIN_ALLOW_ALL=True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'accounts',
    'projects',
    'social_django',#for google oauth authentication
]

MIDDLEWARE = [

    #frontend is written in angular.Requests would originate from different origin
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware', #add this for social auth

]

ROOT_URLCONF = 'project_planner.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',  #these are for social oauth
                'social_django.context_processors.login_redirect', 
            ],
        },
    },
]

WSGI_APPLICATION = 'project_planner.wsgi.application'

#using custom user model instead of django default
AUTH_USER_MODEL="accounts.User"

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'profile'



#for google oauth2...
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


SOCIAL_AUTH_PIPELINE = (
    
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    #disabled by default,but important if email is unique
    #like I have done because otherwise,it will throw error
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = google_conf.GOOGLE_KEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = google_conf.GOOGLE_SECRET


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'latest_ufaber',
        'USER':'sunilpie',
        'PASSWORD':'sunilpie',
        'HOST':'localhost',
    }
}


#rest framework settings
REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': (
       'rest_framework.permissions.IsAdminUser',
        #default permission
        
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (

        #user is identified by server in each request by sending JSON Web access token generated
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        #'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        #'rest_framework.authentication.SessionAuthentication',
        #'rest_framework.authentication.BasicAuthentication',
    ),

    'NON_FIELD_ERRORS_KEY': 'detail',

    #uncomment below when in production phase.Just for testing...
    """
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',],#requests will be accepted with only JSON data unless overriden
    """

    #comment some of the options below from security perspective
     'DEFAULT_RENDERER_CLASSES': [
        
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.AdminRenderer',
    ],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',

    'PAGE_SIZE': 10,

    #'EXCEPTION_HANDLER':('accounts.api.exceptions.base_exception_handler'),

    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],

    'DEFAULT_THROTTLE_RATES': {
        'anon': '20/hour',
        'user': '50/hour'
    }


}



# JWT settings
from datetime import timedelta
SIMPLE_JWT = {

    'ACCESS_TOKEN_LIFETIME': timedelta(hours=24),

    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=1),

    'ROTATE_REFRESH_TOKENS': False,

    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    
    'SIGNING_KEY': SECRET_KEY,
    #'SIGNING_KEY': os.getenv('SECRET_KEY'),

    'VERIFYING_KEY': None,

    'AUDIENCE': None,

    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer'),

    'USER_ID_FIELD': 'id',

    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),

    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',

    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=1),

    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(minutes=1),
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#to run locally,use below settings,including MEDIA_ROOT and MEDIA_URL
STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
