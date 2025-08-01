from django.conf import settings
from django.db import models
from thoughtsapi.models import Topic


class Entry(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='entries'
    )
    title = models.CharField(max_length=255)
    reflection = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isPrivate = models.BooleanField(default=False)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.title)
