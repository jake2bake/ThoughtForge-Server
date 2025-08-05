from django.db import models
from thoughtsapi.models import User

class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shares")
    entry = models.ForeignKey('thoughtsapi.Entry', on_delete=models.CASCADE, related_name="shares", null=True, blank=True)
    reading = models.ForeignKey('thoughtsapi.Reading', on_delete=models.CASCADE, related_name="shares", null=True, blank=True)
    course = models.ForeignKey("thoughtsapi.Course", on_delete=models.CASCADE, related_name="shares", null=True, blank=True)
    shared_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        if not any([self.entry, self.reading, self.course]):
            raise ValidationError("A share must include at least one of: entry, reading, or course.")
        if sum(bool(x) for x in [self.entry, self.reading, self.course]) > 1:
            raise ValidationError("Only one of entry, reading, or course may be shared at a time.")

    def __str__(self):
        if self.entry:
            return f"{self.user} shared Entry '{self.entry}' to {self.shared_to}"
        elif self.reading:
            return f"{self.user} shared Reading '{self.reading}' to {self.shared_to}"
        elif self.course:
            return f"{self.user} shared Course '{self.course}' to {self.shared_to}"
        return f"{self.user} shared something to {self.shared_to}"
