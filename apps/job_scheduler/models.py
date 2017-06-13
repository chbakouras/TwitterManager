from django.contrib.auth.models import User
from django.db import models


class Job(models.Model):
    type = models.CharField(max_length=30)
    running = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
