from django.contrib import admin

from .models import User, UserRole, UserJob

admin.site.register(User)
admin.site.register(UserRole)
admin.site.register(UserJob)

