from django.db import models
from thoughtsapi.models import User, Entry



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'entry')  # Prevent duplicate likes
