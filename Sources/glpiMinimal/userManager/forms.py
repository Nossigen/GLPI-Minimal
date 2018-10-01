from django import forms
from django.forms import ModelForm

from .models import User, UserRole, UserJob

class RoleForm(forms.ModelForm):
    class Meta:
         model = UserRole
         fields = '__all__'

class JobForm(forms.ModelForm):
    class Meta:
         model = UserRole
         fields = '__all__'

class UserForm(forms.ModelForm):

    class Meta:
         model = User
         fields = '__all__'
         # widgets = {
         #    'userRole': forms.Select(choices = UserRole.objects.all(),
         #                             attrs = {'class': 'form-control'}),
         #     'userJob': forms.Select(choices = UserJob.objects.all(),
         #                             attrs = {'class': 'form-control'}),
         # }

    userRole     = forms.ModelChoiceField(queryset = UserRole.objects.all())
    userJob     = forms.ModelChoiceField(queryset = UserJob.objects.all())

    # forname     = forms.CharField(label = 'Prénom',
    #                               max_length = 255)
    # name        = forms.CharField(label = 'Nom',
    #                               max_length = 255)
    # email       = forms.EmailField(label = 'Email',
    #                                max_length = 255,
    #                                widget = forms.EmailInput,
    #                                required = False)
    # oAuthKey    = forms.CharField(label = 'AuthKey',
    #                               max_length = 1024)

    # entryDate   = forms.DateField(label = 'Date d\'entrée dans l\'entreprise',
    #                               widget = forms.DateInput,
    #                               required = False)
    # outDate     = forms.DateField(label = 'Date de sortie de l\'entreprise',
    #                               widget = forms.DateInput,
    #                               required = False)

    # # Links

    # def edit    (self, user_id):
    #     user = User.objects.get(pk = user_id)

    #     self.forname     = forms.CharField(label = 'Prénom',
    #                                        max_length = 255,
    #                                        initial = user.forname)
    #     self.name        = forms.CharField(label = 'Nom',
    #                                        max_length = 255,
    #                                        initial = user.name)
    #     self.email       = forms.EmailField(label = 'Email',
    #                                         max_length = 255,
    #                                         widget = forms.EmailInput,
    #                                         required = False,
    #                                         initial = user.email)
    #     self.oAuthKey    = forms.CharField(label = 'AuthKey',
    #                                        max_length = 1024,
    #                                        initial = user.oAuthKey)

    #     self.entryDate   = forms.DateField(label = 'Date d\'entrée dans l\'entreprise',
    #                                        widget = forms.DateInput,
    #                                        required = False,
    #                                        initial = user.entryDate)
    #     self.outDate     = forms.DateField(label = 'Date de sortie de l\'entreprise',
    #                                        widget = forms.DateInput,
    #                                        required = False,
    #                                        initial = user.outDate)

    #     # Links
    #     self.userRole    = forms.ChoiceField(label = 'Role',
    #                                          choices = UserRole.objects.values_list('pk', 'name'),
    #                                          initial = user.userRole.pk)
    #     self.userJob     = forms.ChoiceField(label = 'Job',
    #                                          choices = UserJob.objects.values_list('pk', 'name'),
    #                                          initial = user.userJob.pk)

