from django             import forms
from django.forms       import ModelForm, formset_factory

from .models                    import User, UserRole, UserJob
from .models                    import Object, ObjectData
from .models                    import ObjectType, ObjectDataType
from .models                    import ObjectHistory, ObjectState

from .models                    import Vendor, Command, CommandState

####################

##########
# Object #
##########

####################

class           ObjectDataForm(forms.ModelForm):

    hidden = forms.IntegerField()

    class       Meta:
        model   = ObjectData
        fields  = ['value']
        labels = {
            'value': 'Valeur',
        }

ObjectDataFormSet = formset_factory(ObjectDataForm, extra = 0)

class           ObjectTypeForm(forms.ModelForm):
    name = forms.CharField(min_length = 4, max_length = 255)
    
    class       Meta:
        model = ObjectType
        fields = ['name']
        labels = {
            'name': 'Nom',
        }


class           ObjectDataTypeForm(forms.ModelForm):
    class       Meta:
        model = ObjectDataType
        fields = ['name', 's_type', 'mendatory', 'visible']
        exclude = ['objectType']
        labels = {
            'name': 'Nom',
            's_type': 'Type de donnée',
            'mendatory': 'Obligatoire',
            'visible': 'Visible'
        }


ObjectDataTypeFormSet = formset_factory(ObjectDataTypeForm, extra = 0)

class           ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = ['name', 'user', 'objectType']
        exclude = ['depth', 'objectIn', 'command', 'user']
        labels = {
            'name': 'Nom',
            'user': 'Utilisateur',
            'objectType': 'Type d\'object'
        }

####################

###########
# History #
###########

####################

class           ObjectToStockForm(forms.ModelForm):
    class Meta:
        model = ObjectHistory
        fields = ['date', 'comment', 'position', 'objectState']
        exclude = ['user', 'objectShown']
        labels = {
            'date': 'Date de remise',
            'comment': 'Commentaire',
            'position': 'Lieu de remise',
            'objectState': 'Etat de l\'object'
        }

class           ObjectToUserForm(forms.ModelForm):
    class Meta:
        model = ObjectHistory
        fields = ['date', 'position', 'objectState', 'user']
        exclude = ['objectShown', 'comment']
        labels = {
            'date': 'Date de remise',
            'position': 'Lieu de remise',
            'objectState': 'Etat de l\'object',
            'user': 'Utilisateur'
        }

class           ObjectStateForm(forms.ModelForm):
#    CHOICES = (
#        ('1', '#1b5e20'),
#        ('2', '#388e3c'),
#       ('3', '#4caf50'),
#        ('4', '#8bc34a'),
#        ('5', '#cddc39'),
#        ('6', '#ffeb3b'),
#        ('7', '#fbc02d'),
#        ('8', '#f57f17'),
#        ('9', '#ff5722'),
#        ('10', '#f44336')
#    )
#    color = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = ObjectState
        fields = ['name', 'color']
        labels = {
            'name': 'Nom',
            'color': 'Couleur'
        }

####################

########
# User #
########

####################

class RoleForm(forms.ModelForm):
    class Meta:
        model = UserRole
        fields = ['name']
        labels = {
            'name': 'Nom'
        }
        
class JobForm(forms.ModelForm):
    class Meta:
         model = UserRole
         fields = ['name']
         labels = {
            'name': 'Nom'
         }

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['forname', 'name', 'email', 'oAuthKey', 'entryDate', 'outDate', 'userRole', 'userJob']
        labels = {
            'forname': 'Prénom',
            'name': 'Nom',
            'email': 'Email',
            'oAuthKey': 'Clef d\'identification',
            'entryDate': 'Date d\'arrivé',
            'outDate': 'Date de départ',
            'userRole': 'Rôle',
            'userJob': 'Poste'   
        }

class VendorForm(forms.ModelForm):
    class Meta:
         model = Vendor
         fields = ['name', 'adress', 'email', 'comment']
         labels = {
            'name': 'Nom',
            'adress': 'Adresse de l\'entreprise',
            'email': 'Email du contact',
            'comment': 'Informations additionnelles'
         }

class CommandForm(forms.ModelForm):

    class Meta:
        model = Command
        fields = '__all__'
        exclude = ['commandState']

class   Command__object_form(forms.ModelForm):

    count = forms.IntegerField(min_value = 1, required = 1)

    class Meta:
        model = Object
        fields = ['name', 'objectType', 'count']

command_object_formset = formset_factory(Command__object_form, extra = 0)

class   Command__object_data_form(forms.ModelForm):
    class Meta:
        model = ObjectData
        fields = ['value', 'objectDataType']

command_object_data_formset = formset_factory(Command__object_data_form, extra = 0)

# Login
class   LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
