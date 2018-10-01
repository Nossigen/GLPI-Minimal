from django.shortcuts   import render
from django.http        import HttpResponse
from django.shortcuts import redirect

from .models            import User, UserRole, UserJob
from .forms             import UserForm, RoleForm, JobForm

from datetime           import date

##################
# List elem part #
##################

# Users
def user_list(request):
    listName = "Liste des utilisateurs"

    # Get the users
    userList = User.objects.order_by('name')
    userListJob = User.objects.order_by('userJob')
    userListRole = User.objects.order_by('userRole')

    viewParams = {
        'listName' : listName,
        'userList' : userList,
        'userListJob' : userListJob,
        'userListRole' : userListRole,
        'today' : date.today(),
        }
    return render(request, 'user_list.html', viewParams)

####################
# Create elem part #
####################

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

            newUser = User.objects.create(name = userName,
                                         forname = userForname,
                                         email = userEmail,
                                         oAuthKey = userOAuthKey,
                                         entryDate = userEntryDate,
                                         outDate = userOutDate,
                                         userRole = userRole,
                                         userJob = userJob)
            newUser.save()

            viewParams = {
                'title': "Nouvel utilisateur",
                'htitle': "Utilisateur " + newUser.name + " " + newUser.forname + " créé",
                'link': "/user/list",
            }
            return render(request, 'redirect.html', viewParams)
        else:
            return render(request, 'new/user.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'new/user.html', {'form': form})


def job_new(request):
    if request.method == 'POST':
        form = JobForm(request.POST)

        # Add to database
        if form.is_valid():

            jobName = form.cleaned_data['name']

            newJob = UserJob.objects.create(name = jobName)
            newJob.save()

            return HttpResponse("Added")
    else:
        form = JobForm()
        return render(request, 'new/job.html', {'form': form})

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
        return render(request, 'new/role.html', {'form': form})

##################
# Edit elem part #
##################

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
        return render(request, 'user_edit.html', {'form': form, 'user_id': user_id})

def job_edit(request, job_id):
    return HttpResponse("Not available")

def role_edit(request, role_id):
    return HttpResponse("Not available")

#####################
# Data of elem part #
#####################

def user_info(request, user_id):

    user = User.objects.get(pk = user_id)

    viewParams = {
        'user' : user,
        'today' : date.today(),
        }


    return render(request, 'user_description.html', viewParams)

####################
# Delete elem part #
####################

def user_delete(request, user_id):

    user_deleted = User.objects.get(pk = user_id)
    User.objects.filter(pk = user_id).delete()

    viewParams = {
        'title': "Utilisateur supprimé",
        'htitle': "Utilisateur " + user_deleted.name + " " + user_deleted.forname + " supprimé",
        'link': "/user/list",
    }

    return render(request, 'redirect.html', viewParams)
