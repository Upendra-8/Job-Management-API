from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=255)
    experience = models.IntegerField()

    def __str__(self):
        return self.title
