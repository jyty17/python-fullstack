from django.db import models
from django.utils import timezone

import datetime

from django.contrib.auth.models import User

class Uploads(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	filename = models.CharField(max_length=150)
	description = models.CharField(max_length=300, default='')
	date_uploaded = models.DateTimeField('date_published', auto_now_add=True)
	last_opened = models.DateTimeField('last_opened', auto_now=True)
	# last_used = 
	is_valid = models.BooleanField(default=True)

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

class CompetitionProfile(models.Model):
	competition_name = models.CharField(max_length=100)
	admin = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=200, default='Welcome!')
	date_created = models.DateTimeField(auto_now_add=True)
	start_datetime = models.DateTimeField(blank=True, null=True)
	end_datetime = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return f'{self.competition_name} created by {self.admin} on {self.date_created}'