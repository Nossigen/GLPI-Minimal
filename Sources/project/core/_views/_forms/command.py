from ..forms    import *

STOCK_USER_ROLE, none = UserRole.objects.get_or_create(name = '__STOCK__')
STOCK_USER_JOB, none = UserJob.objects.get_or_create(name = '__STOCK__')

STOCK_USER, none = User.objects.get_or_create (
                                        name = '__STOCK__',
                                        forname = '__STOCK__',
                                        oAuthKey = '__STOCK__',
                                        userRole = STOCK_USER_ROLE,
                                        userJob = STOCK_USER_JOB
                                    )

DEFAULT_COMMAND_STATE, none = CommandState.objects.get_or_create(name = 'Commandé')

def command_new(request):
    
    if request.method == 'POST':
        form                = CommandForm(request.POST)
        formObject          = command_object_formset(request.POST)
        formsetObjectData   = command_object_data_formset(request.POST)

        select_object_type  = ObjectType.objects.all().select_related()

        print (form)
        print ('----')
        print ('formObject')
        print (formObject)
        print ('----')
        print ('formObjectData')
        print (formsetObjectData)

        if form.is_valid() and formObject.is_valid() and formsetObjectData.is_valid():
            vendor = form.cleaned_data['vendor']
            reference = form.cleaned_data['reference']

#            new_command = Command.objects.create(
#                    reference = form.cleaned_data['reference'],
#                    vendor = form.cleaned_data['vendor'],
#                    commandState = DEFAULT_COMMAND_STATE
#            )

            object_data_type_pos = 0
            j = 0
            print('------')
            print(len(formObject))
            print(len(formsetObjectData))
            print('------')
            while j < len(formObject):
                current_object = formObject[j]
                print('------')
                print(current_object)
                print('------')

                number_to_loop = current_object.cleaned_data['count']

                print('------')
                object_data_types = ObjectDataType.objects.filter(objectType = formObject[j].cleaned_data['objectType'])

                for object_data_type in object_data_types:
                    print('---')
                    print(object_data_type)
                    print('---')
                print('-------')

                loop = 0
                while loop < number_to_loop:
                    loop = loop + 1
                j = j + 1


#                    Object.objects.create(
#                        name    = formObject[j].cleaned_data['name'],
#                        depth   = 0,
#                        user    = STOCK_USER,
#                        command = new_command,
#                        objectType = formObject[j].cleaned_data['objectType'],
#                    )

                    


#                i = 0
#                while i < len(formsetObjectData):

#                    print('/-----/')
#                    print(i)
#                    print(formsetObjectData[i].cleaned_data['value'])
#                    print(formsetObjectData[i].cleaned_data['objectDataType'])
#                    print('/-----/')
#                    i = i + 1

 #                   print('#------#')
  #                  print('Nouvel object: ' + str(loop))
   #                 print('Nom:')
  #                  print(formObject[j].cleaned_data['name'])
   #                 print('De type:')
    #                print(formObject[j].cleaned_data['objectType'].name)
     #               print('Nombre commandé:')
      #              print(formObject[j].cleaned_data['count'])
       #             print('#------#')

#            for objects in formObject:
#                print('#------#')
#                print('Nouvel object:')
#                print('Nom:')
#                print(objects.cleaned_data['name'])
#                print('De type:')
#                print(objects.cleaned_data['objectType'].name)
#                print('Nombre commandé:')
#                print(objects.cleaned_data['count'])
#                print('#------#')

    else:
        form                = CommandForm()
        formObject          = command_object_formset
        formsetObjectData   = command_object_data_formset

        select_object_type  = ObjectType.objects.all().select_related()

    viewParams = {
        'navTitle'              : "Nouvelle commande",

        'form'                  : form,
        'formset_object'        : formObject,
        'formset_object_data'   : formsetObjectData,

        'select_object_type'    : select_object_type
    }
    return render(request, 'forms/command_new.html', viewParams)
