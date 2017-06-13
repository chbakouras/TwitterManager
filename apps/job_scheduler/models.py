from django.contrib.auth.models import User
from django.db import models


class Job(models.Model):
    type = models.CharField(max_length=30)
    finished = models.BooleanField(default=False)
    extra_data = models.TextField(max_length=254)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
