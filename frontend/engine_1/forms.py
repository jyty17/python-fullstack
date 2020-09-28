from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Uploads

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'rows': 5}))



class CreateUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = [
			"first_name",
			"last_name",
			"username",
			"email",
			"password1",
			"password2"
		]

	def save(self, commit=True):
		user = super(CreateUserForm, self).save(commit=False)
		user.email = self.cleaned_data.get("email")
		if commit:
			user.save()
		return user

class EditUserForm(UserChangeForm):
	class Meta:
		model = User
		fields = ["first_name", "last_name", "username", "email"]
		exclude = ["password",]


class UploaderForm(ModelForm):
	class Meta:
		model = Uploads
		fields = ["filename", "description"]


	def save(self, commit=True):
		upload = super(UploaderForm, self).save(commit=False)
		# user = User
		
		if commit:
			print(upload)
			upload.save()
		return upload
		# data = {
		# 	'user_id': '',
		# 	'filename': '',
		# 	'description': '',
		# }
