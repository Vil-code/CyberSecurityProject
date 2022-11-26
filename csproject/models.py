from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	likes = models.IntegerField()
	profile = models.CharField(max_length=100, default="")