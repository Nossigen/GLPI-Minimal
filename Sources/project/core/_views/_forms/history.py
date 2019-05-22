from ..forms            import *

BASE_OBJECT_STATE, none = ObjectState.objects.get_or_create(name = '__NEW__', color = '#f5f5f5')

STOCK_USER_ROLE, none = UserRole.objects.get_or_create(name = '__STOCK__')
STOCK_USER_JOB, test2 = UserJob.objects.get_or_create(name = '__STOCK__')

STOCK_USER, none = User.objects.get_or_create(name = '__STOCK__',
                                        forname = '__STOCK__',
                                        oAuthKey = '__STOCK__',
                                        userRole = STOCK_USER_ROLE,
                                        userJob = STOCK_USER_JOB,
                                        )

def object_to_stock(request, object_id):
    object_selected = Object.objects.get(ref = object_id)
    user_selected = object_selected.user

    if request.method == 'POST':
        form = ObjectToStockForm(request.POST)

        print('')
        print('POST')
        print('')

        if (form.is_valid()):
            nUser           = User.objects.get(pk = user_selected.pk)
            ObjectShown     = Object.objects.get(pk = object_selected.pk)
            Date            = form.cleaned_data['date']
            Comment         = form.cleaned_data['comment']
            Postion         = form.cleaned_data['position']
            ObjectState     = form.cleaned_data['objectState']
            newObjectHistory = ObjectHistory.objects.create(
                comment     = Comment,
                date        = Date,
                position    = Postion,
                objectState = ObjectState,
                user        = nUser,
                objectShown = ObjectShown
            )
            ObjectShown.user = User.objects.get(name = '__STOCK__', forname = '__STOCK__')
            ObjectShown.save()
            data = {
                'history': newObjectHistory,
            }
            pdf = render_to_pdf('pdf/get_back_form.html', data)
            return HttpResponse(pdf, content_type='application/pdf')
    else:
        form = ObjectToStockForm()
    default_values = {
        'object'    : object_selected,
        'user'      : user_selected  
    }
    viewParams = {
        'navTitle'              : "Formulaire de restitution",
        'title'                 : "Formulaire de restitution",
        'form'                  : form,
        'default_values'        : default_values,
    }
    return render(request, 'forms/history_to_stock.html', viewParams)

def object_to_user(request, object_id):
    object_selected = Object.objects.get(ref = object_id)

    if request.method == 'POST':
        form = ObjectToUserForm(request.POST)

        if (form.is_valid()):
            print(form.cleaned_data['objectState'])
            ObjectShown         = Object.objects.get(pk = object_selected.pk)
            new_history = ObjectHistory.objects.create(
                date        = form.cleaned_data['date'],
                position    = form.cleaned_data['position'],
                objectState = form.cleaned_data['objectState'],
                user        = form.cleaned_data['user'],
                objectShown = object_selected
            )
            object_selected.user = form.cleaned_data['user']
            object_selected.save()
            data = {
                'history': new_history,
            }
            pdf = render_to_pdf('pdf/give_form.html', data)
            return HttpResponse(pdf, content_type='application/pdf')
    else:
        form = ObjectToUserForm()
    default_values = {
        'object': object_selected,
    }
    viewParams = {
        'navTitle'              : "Formulaire de remise",
        'title'                 : "Formulaire de remise",
        'form'                  : form,
        'default_values'        : default_values,
    }
    return render(request, 'forms/history_to_user.html', viewParams)

def object_state_new(request):

    if request.method == 'POST':
        form = ObjectStateForm(request.POST)

        if (form.is_valid()):
            newState = ObjectState.objects.create(
                name    = form.cleaned_data['name'],
                color   = form.cleaned_data['color']
            )
            viewParams = {
                'title'     : "Nouvel êtat créé",
                'htitle'    : "Nouvel êtat créé",
                'link'      : "/object/state/new",
            }
            return render(request, 'redirect.html', viewParams)
    else:
        form = ObjectStateForm()
    viewParams = {
        'navTitle'              : "Nouveau êtat de matériel",
        'form'                  : form,
    }
    return render(request, 'forms/object_state_new.html', viewParams)