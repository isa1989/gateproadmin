"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.17.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-i&_0t-+z4ie3u7l(2q3gb2h^x#=frouvd=i_o03sj8kv&n@kj$"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "modeltranslation",
    "django.contrib.admin",
    "rest_framework",
    "customer",
    "device",
    "product",
    "faq",
    "notification",
    "solo",
    "settings",
    "ckeditor",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "gateproadmin.urls"

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ]
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "gateproadmin.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"),
            "USER": os.getenv("DATABASE_USER"),
            "PASSWORD": os.getenv("DATABASE_PASS"),
            "HOST": os.getenv("HOST"),
            "PORT": os.getenv("PORT"),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

# Languages supported
LANGUAGES = [
    ("az", "Azerbaijani"),
    ("en", "English"),
    ("ru", "Russian"),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = "en"


USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = "/static/"

# Ek statik dosya dizinleri
STATIC_ROOT = BASE_DIR / "static/"


# Statik dosyaların toplandığı dizin (genellikle 'collectstatic' komutu ile kullanılır)
# STATIC_ROOT = BASE_DIR / "staticfiles"

# MEDIA_URL = '/media/'
# MEDIA_ROOT = '/app/media/'


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.mail.ru"  # e.g., 'smtp.gmail.com'
# EMAIL_PORT = 465  # Port for SMTP
# EMAIL_USE_TLS = True  # True if using TLS, False otherwise
# EMAIL_HOST_USER = "noreply@oilink.io"  # Your email address
# EMAIL_HOST_PASSWORD = (
#     "G9HHv7TBGeLr3f5tvifx"  # Your email password or application-specific password
# )
# DEFAULT_FROM_EMAIL = "noreply@oilink.io"  # Default sender email
EMAIL_HOST = "smtp.mail.ru"
EMAIL_PORT = 465
EMAIL_HOST_USER = "noreply@oilink.io"  # mail ünvanı
EMAIL_HOST_PASSWORD = "G9HHv7TBGeLr3f5tvifx"  # mailin şifrəsi
EMAIL_USE_SSL = True
