from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    email_verified = models.BooleanField(default=False, verbose_name=_('Email Verified'))

    def __str__(self):
        return self.username
