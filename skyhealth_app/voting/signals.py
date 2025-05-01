#Author - Md Hoque


from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Session, Team, HealthVote

# Used when either session or team is deleted from django admin which then automatically deletes from healthvotes 
# this also updates the votes shown on the html page of sesssions/
@receiver(post_delete, sender=Session)
def cleanup_votes_for_session(sender, instance, **kwargs): #Sender = session class which sends the signal, instance is what was deleted from session, kwargs is used to handle undefined arguments 
    HealthVote.objects.filter(
        session_name=instance.name,
        session_date=instance.date
    ).delete()

@receiver(post_delete, sender=Team)
def cleanup_votes_for_team(sender, instance, **kwargs): # same function as above but for teams
    HealthVote.objects.filter(team_name=instance.name).delete()