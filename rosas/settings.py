"""
Django settings for rosas project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*onw2vnu$f=19p6$$up8$+b-3c$75d6rwx3^6(=c3y6ed9@k9w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic', 
    'fundaciones',
    'Adolescentes',
]
CSRF_TRUSTED_ORIGINS = ['https://rosas-production.up.railway.app']
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]




ROOT_URLCONF = 'rosas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], 
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
JAZZMIN_SETTINGS = {
    "site_title": "Rosas",
    "site_brand": "Rosas",
    "custom_css": "css/custom_jazzmin.css",
    "custom_js": None,
    "show_ui_builder": True,
    "site_logo": "img/LOGO4.png",
    "login_logo": "img/texto-logo.png",
    "site_icon": "img/LOGO3.png",
    "site_logo_classes": "null",
    "welcome_sign": "¡Bienvenidos!. Ingresa tus credeciales para comenzar.",
    "copyright": "Code Busters 🚀 Made with ❤️ ",
    "search_model": ["auth.User", "auth.Group"], 
    # "topmenu_links": [

    # # Url that gets reversed (Permissions can be added)
    # {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

    # # external url that opens in a new window (Permissions can be added)
    # {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

    # # model admin to link to (Permissions checked against model)
    # {"model": "auth.User"},

    # # App with dropdown menu to all its models pages (Permissions checked against models)
    # {"app": "books"},
    # ],
}

JAZZMIN_UI_TWEAKS = {

    "accent": "nav-header-text",
    "sidebar": ".li.nav-item.p a.nav-link.i",
    "sidebar_nav_flat_style": True,
    "theme": "lux",
    "sidebar": "sidebar-light-lightblue",

}

WSGI_APPLICATION = 'rosas.wsgi.application'
LOGIN_URL = ''
LOGOUT_REDIRECT_URL = ''
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'JvKJvJOdjyKsQhGVKNTVGLBiDBKhxgvK',
        'HOST': 'viaduct.proxy.rlwy.net',
        'PORT': '52216',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
