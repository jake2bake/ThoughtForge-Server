from django.db import models

class ReadingAssignment(models.Model):
    due_date = models.DateField()
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=150)
    course = models.ForeignKey("thoughtsapi.Course", on_delete=models.CASCADE, related_name="reading_assignments")
