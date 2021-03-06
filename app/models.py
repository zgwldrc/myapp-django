from django.db import models
from django.utils import timezone
from django.contrib.auth import models as auth_models


class AccountType(models.Model):
    type = models.CharField(max_length=50, unique=True)

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
    owner = models.ForeignKey(auth_models.User, db_column='user_id', default=1)

    class Meta:
        ordering = ['-created_at']




