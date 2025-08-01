from django.db import models
from thoughtsapi.models import Reading, User

class ReadingAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reading_assignments")
    reading = models.ForeignKey(Reading, on_delete=models.CASCADE, related_name="assignments")
    assigned_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
