from django.apps import AppConfig


class ClientdataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clientdata'
    verbose_name = 'Banco de informaciones'

    def ready(self):
        import clientdata.signals