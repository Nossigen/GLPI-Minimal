from datetime import date

from django.http 		import HttpResponse
from django.shortcuts 	import render

from ..models import Object, ObjectType, ObjectData
from ..models import User


def admin(request) :
	objectsStock = Object.objects.filter(user__name = '__STOCK__') \
	    .order_by('objectType')

	objectsAssigned = Object.objects.all() \
		.exclude(user__name__contains = '__') \
		.order_by('objectType')

	for objectAssigned in objectsAssigned :
		objectAssigned.state = objectAssigned.last_history().objectState

	for objectStock in objectsStock :
		objectStock.state = objectStock.last_history().objectState

	objectTypes = ObjectType.objects.all()

	userNumber = User.objects.all().count()

	view_params = {
			'objects_stock'    : objectsStock,
			'objects_assigned' : objectsAssigned,
			'object_types'     : objectTypes,
			'user_number'      : userNumber
			}

	return render(request, 'infos/admin.html', view_params)


def user_info(request, user_id) :
	user = User.objects.get(pk = user_id)
	user_objects = Object.objects.filter(user = user_id)
	datas = ObjectData.objects.all()

	view_params = {
			'title'   : user.forname + ' ' + user.name + ' - Info',
			'user'    : user,
			'today'   : date.today(),
			'objects' : user_objects,
			'datas'   : datas
			}

	return render(request, 'infos/user.html', view_params)


def object_info(request, object_id) :
	object = Object.objects.get(pk = object_id)
	objectData = ObjectData.objects.filter(item = object)

	viewParams = {
			'title'      : object.name + ' - Info',
			'object'     : object,
			'objectData' : objectData,
			}

	return render(request, 'infos/object.html', viewParams)


def vendor_info(request, vendor_id) :
	return HttpResponse('not implemented')


def command_info(request, command_id) :
	return HttpResponse('not implemented')
