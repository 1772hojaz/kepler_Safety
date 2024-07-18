from django.apps import AppConfig


class KesaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kesa'

    def ready(self):
        # Import admin here is safe as it happens after the app registry is ready
        from django.contrib import admin
        admin.site.site_header = 'KESA'
        admin.site.site_title = 'KESA'