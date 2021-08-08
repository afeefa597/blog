from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.
class blog(models.Model):
	title=models.CharField(max_length=20)
	body=models.CharField(max_length=250)
	