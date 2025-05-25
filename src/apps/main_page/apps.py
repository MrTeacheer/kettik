from django.apps import AppConfig
from django.contrib.auth.apps import AuthConfig


class CustomAuthConfig(AuthConfig):
    verbose_name = "Пользователи и доступ"


class MainPageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.main_page"
    verbose_name = "Главная страница"
