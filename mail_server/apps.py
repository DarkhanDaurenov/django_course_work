from django.apps import AppConfig


class MailServerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mail_server'
    verbose_name = 'сервер рассыллок'
