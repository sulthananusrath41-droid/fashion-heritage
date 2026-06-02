from django.contrib import admin

# Register your models here.
from .models import Gown, Comment, Like, Save, UserProfile

admin.site.register(Gown)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Save)
admin.site.register(UserProfile)