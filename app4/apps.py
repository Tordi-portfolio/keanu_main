from django.apps import AppConfig


class App4Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app4'

    def ready(self):
        import app4.signals