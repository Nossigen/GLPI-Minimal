from django.shortcuts   import render
from django.http        import HttpResponse
from django.shortcuts   import redirect

from ..models            import User, UserRole, UserJob
from ..models            import Object, ObjectType, ObjectDataType, ObjectData
from ..models            import Vendor

from django.core.serializers import serialize
from django.http        import JsonResponse
from datetime           import date
from array              import array

################

########
# USER #
########

################

def user_list_options():

    to_return = [
        {
            'name' : 'Tous',
            'ref' : '/user/'
        },
        {
            'name' : 'Par job',
            'ref' : '/user/job'
        },
    ]

    return (to_return)

def user_list(request):
    # Get the users
    userList = User.objects.exclude(userRole = UserRole.objects.get(name = '__STOCK__')).order_by('name')

    viewOption = user_list_options()

    viewParams = {
        'navTitle': 'Liste des utilisateurs',
        'navLinks' : viewOption,
        'navLinkActive' : 'Tous',  

        'userList' : userList,
        'today' : date.today(),
        }
    return render(request, 'list/user.html', viewParams)

def user_list_job(request):
    # Get the users
    userListJob = User.objects.exclude(userRole = UserRole.objects.get(name = '__STOCK__')).order_by('userJob')

    viewOption = user_list_options()

    viewParams = {
        'navTitle': 'Liste des utilisateurs',
        'navLinks' : viewOption,
        'navLinkActive' : 'Par job',  

        'userListJob' : userListJob,
        'today' : date.today(),
        }
    return render(request, 'list/user__by_job.html', viewParams)

####################

##########
# Object #
##########

####################

def object_list(request):
    objectList = Object.objects.exclude(user = User.objects.get(name = '__STOCK__')).order_by('objectType')

    for each_object in objectList:
        each_object.state = each_object.last_history()

    viewParams = {
        'title' : 'Liste du matériel',
        'navTitle': 'Liste du matériel attribué',
        'objectList': objectList
    }

    return render(request, 'list/object.html', viewParams)

def object_stock_list(request):
    objectList = Object.objects.filter(user = User.objects.get(name = '__STOCK__')).order_by('objectType')

    for each_object in objectList:
        each_object.state = each_object.last_history()

    viewParams = {
        'title' : 'Stock',
        'navTitle': 'Liste du matériel en stock',
        'objectList': objectList
    }

    return render(request, 'list/object__stock.html', viewParams)

####################

##########
# Vendor #
##########

####################

def command_list(request):
    return render(request, 'main.html')

def vendor_list(request):
    vendorList = Vendor.objects.all()

    viewParams = {
        'title' : 'Liste des fournisseurs',
        'navTitle': 'Liste des fournisseurs',
        'vendor_list': vendorList
    }

    return render(request, 'list/vendor.html', viewParams)
