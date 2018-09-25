from django import forms

from .models import UserRole, UserJob

class RoleForm(forms.Form):

    name        = forms.CharField(label = 'Role',
                                  max_length = 255)

class JobForm(forms.Form):

    name        = forms.CharField(label = 'Job',
                                  max_length = 255)

class UserForm(forms.Form):
    forname     = forms.CharField(label = 'Prénom',
                                  max_length = 255)
    name        = forms.CharField(label = 'Nom',
                                  max_length = 255)
    email       = forms.EmailField(label = 'Email',
                                   max_length = 255,
                                   widget = forms.EmailInput,
                                   required = False)
    oAuthKey    = forms.CharField(label = 'AuthKey',
                                  max_length = 1024)

    entryDate   = forms.DateField(label = 'Date d\'entrée dans l\'entreprise',
                                  widget = forms.DateInput,
                                  required = False)
    outDate     = forms.DateField(label = 'Date de sortie de l\'entreprise',
                                  widget = forms.DateInput,
                                  required = False)

    # Links
    userRole    = forms.ChoiceField(label = 'Role',
                                    choices = UserRole.objects.values_list('pk', 'name'))
    userJob     = forms.ChoiceField(label = 'Job',
                                    choices = UserJob.objects.values_list('pk', 'name'))
