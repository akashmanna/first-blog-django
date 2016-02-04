from django.contrib import admin
from . import models
from blog.models import UserProfile

class EntryAdmin(admin.ModelAdmin):
	list_display = ("title", "created")
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Entry, EntryAdmin )
admin.site.register(UserProfile)
