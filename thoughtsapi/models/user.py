from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    about_me = models.TextField(blank=True)
    role = models.CharField(max_length=50, default='user')  # e.g. 'admin', 'editor', 'reader'
