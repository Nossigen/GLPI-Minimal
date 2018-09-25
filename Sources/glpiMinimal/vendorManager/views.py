from django.shortcuts	import render
from django.http	import HttpResponse

from django.template    import loader

from .models            import Vendor

def index(request):
    return HttpResponse("Index: vendorManager")

def vendor_list(request):
    vendors = Vendor.objects.order_by('name')
    template = loader.get_template('vendorList.html')
    context = {
        'vendor_list' : vendors,
    }
    return HttpResponse(template.render(context, request))
