from django.contrib import admin

from .models import ObjectState, ObjectHistory

admin.site.register(ObjectHistory)
admin.site.register(ObjectState)
