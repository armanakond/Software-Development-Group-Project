#Author - Md Hoque
#Co Author - Junayed Ahmed
#Co Author - Sikandar Ali

from django.apps import AppConfig


#Simple code for the admin dashboard
class VotingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'voting'
    verbose_name = "VOTING"

    def ready(self):
        import voting.signals


