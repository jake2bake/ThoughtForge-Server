from django.db import models

class Submission(models.Model):
    user = models.ForeignKey('thoughtsapi.User', on_delete=models.CASCADE, related_name="submissions")
    reflection = models.CharField(max_length=300)
    submitted_at = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField(null=True, blank=True)
    grade = models.CharField(max_length=2, null=True, blank=True)
    title = models.CharField(max_length=100)
    reading = models.ForeignKey('thoughtsapi.Reading', on_delete=models.CASCADE, related_name="submissions")