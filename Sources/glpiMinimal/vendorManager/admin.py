from django.contrib import admin

from .models import Vendor, Command, CommandState

admin.site.register(Vendor)
admin.site.register(Command)
admin.site.register(CommandState)

