import os
from pathlib import Path
from dotenv import load_dotenv
from .cors import *
from .modeltranslation import *
from .jazzmin import *
from .swagger import *

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG") == "True"
PROD = os.getenv("PROD") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
if PROD:
    from .prod import *
else:
    from .dev import *

# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # packages
    "rest_framework",
    "phonenumber_field",
    "drf_spectacular",
    "django_cleanup.apps.CleanupConfig",
    # apps
    "apps.main_page.apps.MainPageConfig",
    "apps.main_page.apps.CustomAuthConfig",
    "apps.gallary.apps.GallaryConfig",
    "apps.about_us.apps.AboutUsConfig",
    "apps.kyrgystan.apps.KyrgystanConfig",
    "apps.tour.apps.TourConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "core.wsgi.application"


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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


STATIC_URL = "/back_static/"
STATIC_ROOT = os.path.join(BASE_DIR, "back_static")

MEDIA_URL = "/back_media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "back_media")
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}
