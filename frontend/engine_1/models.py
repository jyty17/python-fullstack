from django.db import models
from django.utils import timezone

import datetime

from django.contrib.auth.models import User

class Uploads(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	filename = models.CharField(max_length=200)
	
	date_uploaded = models.DateTimeField('date_published')
	# last_used = 

	def __str__(self):
		return f'{filename}'


class UserProfile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# profile_image = models.ImageField(upload_to='profiles')
	uploads = 0

	def __str__(self):
		return f"{user}'s profile"