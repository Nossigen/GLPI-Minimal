from ..forms    import *

def user_new(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        # Add to database
        if form.is_valid():

            userName            = form.cleaned_data['name']
            userForname         = form.cleaned_data['forname']
            userEmail           = form.cleaned_data['email']
            userOAuthKey        = form.cleaned_data['oAuthKey']

            userEntryDate       = form.cleaned_data['entryDate']
            userOutDate         = form.cleaned_data['outDate']

            userRole            = form.cleaned_data['userRole']
            userJob             = form.cleaned_data['userJob']

            newUser = User.objects.create(
                name        = userName,
                forname     = userForname,
                email       = userEmail,
                oAuthKey    = userOAuthKey,
                entryDate   = userEntryDate,
                outDate     = userOutDate,
                userRole    = userRole,
                userJob     = userJob
            )
            newUser.save()

            viewParams = {
                'title': "Nouvel utilisateur",
                'navTitle': "Nouvel utilisateur",
                'htitle': "Utilisateur " + newUser.name + " " + newUser.forname + " créé",
                'link': "/user",
            }
            return render(request, 'redirect.html', viewParams)
        else:
            return render(request, 'user/new/user.html', {'form': form, 'navTitle': "Nouvel utilisateur"})
    else:
        form = UserForm()
        return render(request, 'forms/user_new.html', {'form': form, 'navTitle': "Nouvel utilisateur"})

def job_new(request):

    valid = False
    jobList = UserJob.objects.all().exclude(name__contains = '__')

    if request.method == 'POST':
        form = JobForm(request.POST)

        # Add to database
        if form.is_valid():

            jobName = form.cleaned_data['name']

            newJob = UserJob.objects.create(name = jobName)
            newJob.save()
            valid = True
            form = JobForm()
    else:
        form = JobForm()

    viewParams = {
        'navTitle': "Nouvel emploi",
        'title': "Nouvel emploi",
        'job_list': jobList,
        'valid': valid,
        'form': form
    }
    return render(request, 'forms/job_new.html', viewParams)

# TODO: Implement
def role_new(request):

    if request.method == 'POST':
        form = RoleForm(request.POST)

        # Add to database
        if form.is_valid():

            roleName = form.cleaned_data['name']

            newRole = UserRole.objects.create(name = roleName)
            newRole.save()

            return HttpResponse("Added")
    else:
        form = RoleForm()
        return render(request, 'forms/role_new.html', {'form': form})

def user_edit(request, user_id):
    if request.method == 'POST':
        form = UserForm(request.POST)

        # Add to database
        if form.is_valid():

            existingUser = User.objects.get(pk = user_id)

            existingUser.name           = form.cleaned_data['name']
            existingUser.forname        = form.cleaned_data['forname']
            existingUser.email          = form.cleaned_data['email']
            existingUser.entryDate      = form.cleaned_data['entryDate']
            existingUser.outDate        = form.cleaned_data['outDate']
            existingUser.userRole       = form.cleaned_data['userRole']
            existingUser.userJob        = form.cleaned_data['userJob']

            existingUser.save()
            return redirect('/user/' + str(user_id))
        else:
            return HttpResponse("Le formulaire est invalide")
    else:
        user = User.objects.get(pk = user_id)
        form = UserForm(instance = user)
        return render(request, 'forms/user_edit.html', {'form': form, 'user_id': user_id})

def job_edit(request, job_id):
    return HttpResponse("Not available")

def role_edit(request, role_id):
    return HttpResponse("Not available")

def user_delete(request, user_id):

    user_deleted = User.objects.get(pk = user_id)
    User.objects.filter(pk = user_id).delete()

    viewParams = {
        'title': "Utilisateur supprimé",
        'htitle': "Utilisateur " + user_deleted.name + " " + user_deleted.forname + " supprimé",
        'link': "/user",
    }

    return render(request, 'redirect.html', viewParams)
