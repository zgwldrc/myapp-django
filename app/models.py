from django.db import models
from django.utils import timezone
from django.contrib.auth import models as auth_models


class AccountType(models.Model):
    type = models.CharField(max_length=50, unique=True)

    def natural_key(self):
        return [self.type]

    class Meta:
        ordering = ['type']


class Account(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    login_url = models.CharField(max_length=150)
    desc = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, db_index=True)

    type = models.ForeignKey(AccountType)
    user = models.ForeignKey(auth_models.User)

    class Meta:
        ordering = ['-created_at']




