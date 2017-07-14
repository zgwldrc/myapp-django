from django.db import models
from django.contrib.auth import models as auth_models


class AccountType(models.Model):
    type = models.CharField(max_length=50)


class Account(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    login_url = models.CharField(max_length=150)
    desc = models.TextField()

    type = models.ForeignKey(AccountType)
    user = models.ForeignKey(auth_models.User)




