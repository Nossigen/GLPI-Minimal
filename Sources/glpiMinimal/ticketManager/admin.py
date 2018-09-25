from django.contrib import admin

from .models import Ticket, TicketState, TicketMessage

admin.site.register(Ticket)
admin.site.register(TicketState)
admin.site.register(TicketMessage)
