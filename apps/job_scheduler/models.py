from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from django.db import models


class Job(models.Model):
    type = models.CharField(max_length=30)
    finished = models.BooleanField(default=False)
    extra_data = models.TextField(validators=[MaxLengthValidator(254)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
