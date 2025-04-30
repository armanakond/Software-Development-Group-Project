from django.db import models

# Create your models here.
# voting/models.py

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Poll"
        verbose_name_plural = "Polls"

    def __str__(self):
        return self.question
