from django.contrib import admin
from .models import *

# Register your models here.
class ThoughtAdmin(admin.ModelAdmin):
    list_display = ("name", "thought", "pic")
admin.site.register(Snippet, ThoughtAdmin)

admin.site.register(UserProfileInfo)