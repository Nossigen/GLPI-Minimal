from django.shortcuts   import render
from django.http        import HttpResponse

from .models            import User, UserRole, UserJob
from .forms             import UserForm, RoleForm, JobForm

##################
# List elem part #
##################

# Users
def user_list(request):
    listName = "Liste des utilisateurs"

    # Get the users
    userList = User.objects.order_by('name')

    viewParams = {
        'listName' : listName,
        'userList' : userList
        }
    return render(request, 'user_list.html', viewParams)

def user_list_by_job(request):
    listName = "Liste des utilisateurs par job"

    # Get the users
    userList = User.objects.order_by('name')

    viewParams = {
        'listName' : listName,
        'userList' : userList
        }
    return render(request, 'user_job_list.html', viewParams)

def user_list_by_role(request):
    listName = "Liste des utilisateurs par rôle"

    # Get the users
    userList = User.objects.order_by('name')

    viewParams = {
        'listName' : listName,
        'userList' : userList
        }
    return render(request, 'user_role_list.html', viewParams)

# User's job

# User's role

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

            userRole            = UserRole.objects.get(pk = form.cleaned_data['userRole'])
            userJob             = UserJob.objects.get(pk = form.cleaned_data['userJob'])

            newUser = User.objects.create(name = userName,
                                         forname = userForname,
                                         email = userEmail,
                                         oAuthKey = userOAuthKey,
                                         entryDate = userEntryDate,
                                         outDate = userOutDate,
                                         userRole = userRole,
                                         userJob = userJob)
            newUser.save()
            return HttpResponse("Added")
        else:
            return HttpResponse("Something is not working")
    else:
        form = UserForm()
        return render(request, 'new_user.html', {'form': form})


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
        return render(request, 'new_job.html', {'form': form})

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
        return render(request, 'new_role.html', {'form': form})

##################
# Edit elem part #
##################

def user_edit(request):
    return HttpResponse("Not available")

def job_edit(request):
    return HttpResponse("Not available")

def role_edit(request):
    return HttpResponse("Not available")

# Data elem part

def user_info(request):
    return HttpResponse("Not available")
