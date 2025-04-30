from django.db import models

# Create your models here.
class AccountEntry(models.Model):
    """
    A dummy model just to show the ACCOUNTS box.
    Replace with real fields later.
    """
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entry at {self.created}"