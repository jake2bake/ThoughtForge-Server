from django.db import models
from thoughtsapi.models import User, Entry

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submissions")
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="submissions")
    submitted_at = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField(null=True, blank=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
