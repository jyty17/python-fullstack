from django.db import models
from django.utils import timezone

import datetime

from django.contrib.auth.models import User

class Uploads(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	filename = models.CharField(max_length=150)
	description = models.CharField(max_length=300, default=filename)
	date_uploaded = models.DateTimeField('date_published')
	last_opened = models.DateTimeField('last_opened')
	# last_used = 

	def __str__(self):
		return f'user: {self.user}, \n \
				filename: {self.filename}, \n \
				description: {self.description} \n \
				date_uploaded: {self.date_uploaded} \n \
				last_opened: {self.last_opened} \n \
				'


class UserProfile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# profile_image = models.ImageField(upload_to='profiles')
	uploads = 0

	def __str__(self):
		return f"{user}'s profile"