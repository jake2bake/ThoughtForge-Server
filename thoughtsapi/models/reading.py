from django.db import models


class Reading(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    topic = models.ForeignKey("thoughtsapi.Topic", on_delete=models.SET_NULL, null=True, blank=True, related_name="readings")
