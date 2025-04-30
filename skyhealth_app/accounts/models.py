from django.db import models
from django.contrib.auth.models import Permission

# Create your models here.
class AccountEntry(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        help_text="Name of this account entry"
    )
    permissions = models.ManyToManyField(
        Permission,
        verbose_name="permissions",
        blank=True,
        help_text="The permissions this account entry grants"
    )

    class Meta:
        verbose_name = "Employees"
        verbose_name_plural = "Employee Entry"

    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.name