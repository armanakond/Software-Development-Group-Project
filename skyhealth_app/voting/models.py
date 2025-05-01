#Author - Junayed Ahmed
#Co Author - Md Hoque
#Co Author - 

from django.db import models
from django.contrib.auth.models import User



#Model.py code for healthvote section of application
class HealthVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_name = models.CharField(max_length=100)
    session_date = models.CharField(max_length=100)
    team_name = models.CharField(max_length=100)

    #Blank and nulls help with both allowing empty aspects in the form and the databases.
    q1_vote = models.CharField(max_length=10, blank=True, null=True)
    q1_feedback = models.TextField(blank=True)
    q1_team_actions = models.TextField(blank=True)
    q1_org_solutions = models.TextField(blank=True)

    q2_vote = models.CharField(max_length=10, blank=True, null=True)
    q2_feedback = models.TextField(blank=True)
    q2_team_actions = models.TextField(blank=True)
    q2_org_solutions = models.TextField(blank=True)

    q3_vote = models.CharField(max_length=10, blank=True, null=True)
    q3_feedback = models.TextField(blank=True)
    q3_team_actions = models.TextField(blank=True)
    q3_org_solutions = models.TextField(blank=True)

    q4_vote = models.CharField(max_length=10, blank=True, null=True)
    q4_feedback = models.TextField(blank=True)
    q4_team_actions = models.TextField(blank=True)
    q4_org_solutions = models.TextField(blank=True)

    q5_vote = models.CharField(max_length=10, blank=True, null=True)
    q5_feedback = models.TextField(blank=True)
    q5_team_actions = models.TextField(blank=True)
    q5_org_solutions = models.TextField(blank=True)

    q6_vote = models.CharField(max_length=10, blank=True, null=True)
    q6_feedback = models.TextField(blank=True)
    q6_team_actions = models.TextField(blank=True)
    q6_org_solutions = models.TextField(blank=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.session_name} - {self.session_date}"
    
#Further code for sessions for the database and forms    
class Session(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.name} ({self.date})"

#Further code for teams for the database and forms
class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name