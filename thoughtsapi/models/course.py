from django.db import models
from thoughtsapi.models import User, Reading

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    readings = models.ManyToManyField(Reading, related_name="courses", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
