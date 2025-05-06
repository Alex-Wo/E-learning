import os
from pathlib import Path

from django.urls import reverse_lazy
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = (os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = (os.getenv('DEBUG'))

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'channels',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'courses.apps.CoursesConfig',
    'students.apps.StudentsConfig',
    'embed_video',
    'redisboard',
    'debug_toolbar',
    'rest_framework',
    'chat',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'elearning.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'elearning.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': (os.getenv('ENGINE')),
        'NAME': (os.getenv('NAME')),
        'USER': (os.getenv('USER')),
        'PASSWORD': (os.getenv('PASSWORD')),
        'HOST': (os.getenv('HOST')),
        'PORT': (os.getenv('PORT')),
    }
}

# Password validation

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

LANGUAGE_CODE = (os.getenv('LANGUAGE_CODE'))

TIME_ZONE = (os.getenv('TIME_ZONE'))  # UTC -3

USE_I18N = (os.getenv('USE_I18N'))

USE_TZ = (os.getenv('USE_TZ'))

# Static files (CSS, JavaScript, Images)

STATIC_URL = (os.getenv('STATIC_URL'))

MEDIA_URL = (os.getenv('MEDIA_URL'))
MEDIA_ROOT = (os.getenv('MEDIA_ROOT'))

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Users

LOGIN_REDIRECT_URL = (os.getenv('LOGIN_REDIRECT_URL'))

# Caches

CACHES = {
    'default': {
        'BACKEND': (os.getenv('BACKEND')),
        'LOCATION': (os.getenv('LOCATION')),
    }
}

INTERNAL_IPS = [
    '127.0.0.1',
]

# Caches settings

CACHE_MIDDLEWARE_ALIAS = (os.getenv('CACHE_MIDDLEWARE_ALIAS'))
CACHE_MIDDLEWARE_SECONDS = (os.getenv('CACHE_MIDDLEWARE_SECONDS'))
CACHE_MIDDLEWARE_KEY_PREFIX = (os.getenv('CACHE_MIDDLEWARE_KEY_PREFIX'))

# Настроечные параметры REST

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# Channels settings

ASGI_APPLICATION = 'elearning.asgi.application'

# Настроечные параметры хранилища связи Redis для канального слоя

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6379)]
        },
    },
}

# Jazzmin admin

JAZZMIN_SETTINGS = {

    "site_title": "Elearning Admin",
    "site_header": "Elearning",
    "site_brand": "Elearning",
    "site_logo": "media/images/logo.png",
    "login_logo": None,
    "login_logo_dark": None,
    "site_logo_classes": "img-circle",
    "site_icon": None,
    "welcome_sign": "Welcome to the Elearning",
    "copyright": "Elearning Ltd",
    "search_model": ["auth.User", "auth.Group"],
    "user_avatar": None,

    # Top Menu

    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "#", "new_window": True},
        {"model": "auth.User"},
        {"app": "Elearning"},
    ],

    # User Menu

    "usermenu_links": [
        {"name": "Support", "url": "#", "new_window": True},
        {"model": "auth.user"}
    ],

    # Side Menu

    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
    "custom_links": {
        "books": [{
            "name": "Make Messages",
            "url": "make_messages",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    # Related Modal

    "related_modal_active": False,

    # UI Tweaks

    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,

    # Change view

    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    "language_chooser": False,
}
