from django.contrib import admin

from .models import CompetitionProfile, Uploads

class CompetitionAdmin(admin.ModelAdmin):
	fields = ["competition_name", "admin", "description", "start_datetime", "end_datetime"]


class UploadAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 		{'fields': ['user', 'filename']}),
		('Valid',	{'fields': ['is_valid']} )
	]

	list_display = ('filename', 'description')

admin.site.register(CompetitionProfile, CompetitionAdmin)
admin.site.register(Uploads, UploadAdmin)