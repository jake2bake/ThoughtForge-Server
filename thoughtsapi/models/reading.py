from django.db import models


class Reading(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    topic = models.ForeignKey("thoughtsapi.Topic", on_delete=models.SET_NULL, null=True, blank=True, related_name="readings")
    course = models.ForeignKey("thoughtsapi.Course", on_delete=models.CASCADE, related_name="courses")
    gutenberg_id = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.title) if self.title else ""
