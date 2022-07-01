from django.apps import AppConfig
from django.db.models import signals


class AdminCommandConfig(AppConfig):
    name = 'admincommand'

    def ready(self):
        from admincommand.management import sync_db_callback
        # This post_migrate signal adds the required Permissions for running admincommands
        signals.post_migrate.connect(sync_db_callback, sender=self)
        super().ready()
