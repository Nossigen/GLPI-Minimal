from ..forms    import *

def vendor_new(request):

    if request.method == 'POST':
        form = VendorForm(request.POST)

        if (form.is_valid()):

            newVendorName       = form.cleaned_data['name']
            newVendorEmail      = form.cleaned_data['email']
            newVendorAdress     = form.cleaned_data['adress']
            newVendorComment    = form.cleaned_data['comment']
            newVendor = Vendor.objects.create(
                name    = newVendorName,
                email   = newVendorEmail,
                adress  = newVendorAdress,
                comment = newVendorComment
            )
            viewParams = {
                'title': "Nouveau fournisseur ajouté",
                'htitle': "Nouveau fournisseur ajouté",
                'link': "/vendor/",                
            }
            return render(request, 'redirect.html', viewParams)

        else:
            viewParams = {
                'navTitle'              : "Nouveau fournisseur",
                'form'                  : form,
            }
            return render(request, 'forms/vendor_new.html', viewParams)
    form = VendorForm()    
    viewParams = {
        'navTitle'              : "Nouveau fournisseur",
        'form'                  : form,
    }
    return render(request, 'forms/vendor_new.html', viewParams)