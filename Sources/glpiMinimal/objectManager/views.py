from django.shortcuts 	import render
from django.http	import HttpResponse

from array import array

# Import object table
from objectManager.models      import Object, ObjectType

def index(request):
    return HttpResponse("Index: objectManager")

# List objects
def object_list(request):
    # Get the primary object
    types = ObjectType.objects.all()
    objectList = Object.objects.filter()

    # Create a list filtered by it's Object.objectType
    objects = 0
    for typeItem in types:

        objectTypeList = 0

        for objectItem in objectList:

            if objectItem.objectType.name == typeItem.name :

                if objectTypeList:
                    objectTypeList.append(objectItem)
                else:
                    objectTypeList = [objectItem]

        if objectTypeList:
            if objects:
                objects.append(objectTypeList)
            else:
                objects = [objectTypeList]

    # Set the values for the template
    viewParams = {
        'objects' : objects,
        'types' : types
        }

    # Send page
    return render(request, 'list.html', viewParams)

# Forms
def add_object(request):
    return HttpResponse("Add object webpage")
