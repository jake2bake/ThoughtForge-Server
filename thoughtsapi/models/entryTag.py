from django.db import models
from thoughtsapi.models import Entry, Tag

class EntryTag(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.entry.title} - {self.tag.name}"
