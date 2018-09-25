from django.shortcuts   import render
from django.http        import HttpResponse


def index(request):
    return HttpResponse("Index: historyManager")

def history_list(request):
    return HttpResponse("History list")
