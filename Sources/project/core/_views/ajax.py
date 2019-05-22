
from django.shortcuts   import render
from django.http        import HttpResponse
from django.shortcuts   import redirect

from ..models            import User, UserRole, UserJob
from ..models            import Object, ObjectType, ObjectDataType, ObjectData

from django.core.serializers    import serialize
from django.http                import JsonResponse

def get_type_form(request):
    type_id = request.GET.get('objectType', None)

    objectTypeSelected = ObjectType.objects.get(pk = type_id)
    objectDataTypes = ObjectDataType.objects.filter(objectType = objectTypeSelected)

    data = {
        'objectType': serialize('json', objectDataTypes)
    }
    return JsonResponse(data)
