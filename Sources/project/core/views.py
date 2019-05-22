from django.shortcuts   import render
from django.http        import HttpResponse
from django.shortcuts   import redirect

#from django.core.serializers import serialize
#from django.http        import JsonResponse
#from datetime           import date
#from array              import array

# List views
from ._views.list       import user_list
from ._views.list       import user_list_job
from ._views.list       import object_list
from ._views.list       import object_stock_list
from ._views.list       import command_list
from ._views.list       import vendor_list

# Form views
from ._views.forms      import user_new
from ._views.forms      import job_new
from ._views.forms      import role_new
from ._views.forms      import object_new
from ._views.forms      import object_type_new
from ._views.forms      import object_to_stock
from ._views.forms      import object_to_user
from ._views.forms      import object_state_new
from ._views.forms      import command_new
from ._views.forms      import vendor_new

from ._views.forms      import user_edit
from ._views.forms      import job_edit
from ._views.forms      import role_edit

from ._views.forms      import user_delete

from ._views.forms      import login

# Info views
from ._views.infos      import user_info
from ._views.infos      import object_info
from ._views.infos      import vendor_info
from ._views.infos      import command_info
from ._views.infos      import admin

# Ajax section
from ._views.ajax       import get_type_form

from .models import User, UserRole, UserJob


# TODO: Clean this check (I'm learning django)

# Check for the basic data
if (not (UserRole.objects.filter(name = '__STOCK__').exists())):
    UserRole.objects.create(name = '__STOCK__')

if (not (UserJob.objects.filter(name = '__STOCK__').exists())):
    UserJob.objects.create(name = '__STOCK__')

if (not (User.objects.filter(name = '__STOCK__', forname = '__STOCK__').exists())):
    User.objects.create(
        name = '__STOCK__',
        forname = '__STOCK__',
        oAuthKey = 'None',
        userRole = UserRole.objects.get(name = '__STOCK__'),
        userJob = UserJob.objects.get(name = '__STOCK__'),
    )

if (not (User.objects.filter(name = '__PENDING__', forname = '__PENDING__').exists())):
    User.objects.create(
        name = '__PENDING__',
        forname = '__PENDING__',
        oAuthKey = 'None',
        userRole = UserRole.objects.get(name = '__STOCK__'),
        userJob = UserJob.objects.get(name = '__STOCK__'),
    )

from .models import Object
def test(request):
    get = Object.objects.get(pk = 'cbe29927-c694-4bec-b776-810bc00af604').last_object_state()
    return HttpResponse('Le dernier état de l\'object est: ' + get.objectState.name)

def index(request):
    return HttpResponse("Index: objectManager")
