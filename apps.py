
from kernel.interfaces.stack import model_ready 
from django.apps import AppConfig


class BootConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "boot"
    
    def ready(self):
        """
        This is called when the app is ready
        """
        # model_ready()
        pass