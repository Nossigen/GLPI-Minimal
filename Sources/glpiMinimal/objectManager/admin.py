from django.contrib import admin

from .models import ObjectType, ObjectDataType, ObjectData, Object

admin.site.register(ObjectType)
admin.site.register(ObjectDataType)
admin.site.register(ObjectData)
admin.site.register(Object)
