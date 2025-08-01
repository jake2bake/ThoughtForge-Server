from django.db import models
from thoughtsapi.models import User, Entry

class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shares")
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="shares")
    shared_with = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
