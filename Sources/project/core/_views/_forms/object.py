from ..forms    import *

STOCK_USER_ROLE, none = UserRole.objects.get_or_create(name = '__STOCK__')
STOCK_USER_JOB, none = UserJob.objects.get_or_create(name = '__STOCK__')


STOCK_USER, none = User.objects.get_or_create(name = '__STOCK__',
                                        forname = '__STOCK__',
                                        oAuthKey = '__STOCK__',
                                        userRole = STOCK_USER_ROLE,
                                        userJob = STOCK_USER_JOB
                                    )

STATE_NEW, none = ObjectState.objects.get_or_create(name = 'Neuf', color = '#2196f3')

def object_new_options():

    to_return = [
        {
            'name' : 'Simple',
            'ref' : '/object/new'
        },
        {
            'name' : 'Type',
            'ref' : '/object/new/type'
        }
    ]

    return to_return

def object_type_new(request):

    if request.method == 'POST':

        formObjectType      = ObjectTypeForm(request.POST)
        formObjectDataType  = ObjectDataTypeFormSet(request.POST)
    
        if (formObjectType.is_valid()):
            if (formObjectDataType.is_valid()):
                newObjectTypeName = formObjectType.cleaned_data['name']
                newObjectType = ObjectType.objects.create(name = newObjectTypeName);
    
                for form in formObjectDataType:
                    # Set new values
                    if (form.is_valid()):
                        newObjectDataTypeName       = form.cleaned_data['name']
                        newObjectDataTypeSType      = form.cleaned_data['s_type']
                        newObjectDataTypeMendatory  = form.cleaned_data['mendatory']
                        newObjectDataTypeVisible    = form.cleaned_data['visible']
                        newObjectDataTypeLink       = newObjectType
        
                        newObjectDataType = ObjectDataType.objects.create(
                            name            = newObjectDataTypeName,
                            s_type          = newObjectDataTypeSType,
                            mendatory       = newObjectDataTypeMendatory,
                            visible         = newObjectDataTypeVisible,
                            objectType      = newObjectDataTypeLink
                            )
                viewParams = {
                    'title': "Nouveau type de matériel ajouté",
                    'navTitle': "Nouveau type de matériel ajouté",
                    'htitle': "Nouveau type de matériel ajouté",
                    'link': "/object/new/",
                }
                return render(request, 'redirect.html', viewParams)

    formObjectType = ObjectTypeForm()
    formsetObjectDataType = ObjectDataTypeFormSet

    viewParams = {
        'navTitle'              : "Nouvel matériel",        
        'navLinks'              : object_new_options(),
        'navLinkActive'         : 'Type',
        'formObjectType'        : formObjectType,
        'formsetObjectDataType' : formsetObjectDataType,
        }
    
    return render(request, 'forms/object_type_new.html', viewParams)
    
# Object
def object_new(request):
    if request.method == 'POST':
        formObject          = ObjectForm(request.POST)
        formObjectData      = ObjectDataFormSet(request.POST)

        print(formObject)
        print(formObjectData)

        if (formObject.is_valid()):
            newObjectName       = formObject.cleaned_data['name']
            newObjectUser       = STOCK_USER
            newObjectType       = formObject.cleaned_data['objectType']
            newObject = Object.objects.create(
                name        = newObjectName,
                user        = newObjectUser,
                objectType  = newObjectType,
                depth       = 0
            )

            if (formObjectData.is_valid()):
                for form in formObjectData :
                    newObjectDataValue      = form.cleaned_data['value']
                    newObjectDataDataType   = form.cleaned_data['hidden']
                    newObjectDataItem       = newObject
                    newObjectDataType       = ObjectDataType.objects.get(pk = newObjectDataDataType)

                    newObjectData           = ObjectData.objects.create(
                        value           = newObjectDataValue,
                        item            = newObjectDataItem,
                        objectDataType  = newObjectDataType
                    )


                # Create a basic state sheet for the new object
                new_history = ObjectHistory.objects.create(
                    comment = "Objet arrivé au sein de l'entreprise",
                    date = "2000-12-12",
                    position = 'Inconnue',
                    objectState = STATE_NEW,
                    user = STOCK_USER,
                    objectShown = newObject
                )
                
                viewParams = {
                    'title': "Nouveau matériel ajouté",
                    'htitle': "Nouveau matériel ajouté",
                    'link': "/object/new",
                }
                return render(request, 'redirect.html', viewParams)
            else:
                newObject.delete()
                viewParams = {
                    'title': "Un matériel ne peut être créer sans attributs",
                    'htitle': "Un matériel ne peut être créer sans attributs",
                    'link': "/object/new",                
                }
                return render(request, 'redirect.html', viewParams)
        else:
            viewParams = {
                'navTitle'              : "Nouvel objet",        
                'navLinks'              : object_new_options(),
                'navLinkActive'         : 'Simple',
                "formObject"            : formObject,
                "formsetObjectData"     : formsetObjectData,
            }
            return render(request, 'redirect.html', viewParams)
    else:
        formObject = ObjectForm()
        formsetObjectData = ObjectDataFormSet

        viewParams = {
                'navTitle'              : "Nouvel objet",        
                'navLinks'              : object_new_options(),
                'navLinkActive'         : 'Simple',
                "formObject"            : formObject,
                "formsetObjectData"     : formsetObjectData,
                'default_user'          : STOCK_USER,
            }

        return render(request, 'forms/object_new.html', viewParams)
