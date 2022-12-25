from django.db import models
from django.contrib.auth.models import AbstractUser

PREFERED_TYPES = (("voice", "voice"), ("text", "text"))

class User(AbstractUser):
    # prefered_type = models.CharField(max_length=50, choices=PREFERED_TYPES, null=True)
    pass

