from django.db import models

class Topic(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return str(self.label)
