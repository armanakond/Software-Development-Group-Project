#Author - Junayed Ahmed
#Co Author - 
#Co Author - 


from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Session, Team, HealthVote


@receiver(post_delete, sender=Session)
def cleanup_votes_for_session(sender, instance, **kwargs):
    HealthVote.objects.filter(
        session_name=instance.name,
        session_date=instance.date
    ).delete()

@receiver(post_delete, sender=Team)
def cleanup_votes_for_team(sender, instance, **kwargs):
    HealthVote.objects.filter(team_name=instance.name).delete()