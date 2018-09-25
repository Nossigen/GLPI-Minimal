from django.shortcuts   import render
from django.http        import HttpResponse


def index(request):
    return HttpResponse("Index: ticketManager")

def ticket_list(request):
    return HttpResponse("Ticket List")
