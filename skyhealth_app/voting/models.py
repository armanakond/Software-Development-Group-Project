from django.conf import settings
from django.db import models

class SurveySubmission(models.Model):
    user       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} @ {self.created_at:%Y-%m-%d %H:%M}"

class SurveyAnswer(models.Model):
    CHOICES = [
        ('green', 'Green'),
        ('amber', 'Amber'),
        ('red',   'Red'),
    ]

    submission      = models.ForeignKey(
                          SurveySubmission,
                          related_name='answers',
                          on_delete=models.CASCADE
                      )
    question_number = models.PositiveSmallIntegerField()
    choice          = models.CharField(max_length=5, choices=CHOICES)
    feedback        = models.TextField(blank=True)
    team_actions    = models.TextField(blank=True)
    org_solutions   = models.TextField(blank=True)

    class Meta:
        ordering = ['submission', 'question_number']

    def __str__(self):
        return f"Q{self.question_number}: {self.choice}"
