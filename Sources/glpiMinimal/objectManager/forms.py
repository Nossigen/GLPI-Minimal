from django     import forms

# Import related table
from .models                    import Object, ObjectType
from userManager.models         import User
from vendorManager.models       import Command

class           addObjectForm(forms.Form):

    # Object definition
    objectName  = models.CharField(max_length = 255)
    depth       = 0
    objectIn    = ManyToManyField('self', blank = True)

    # Object related to:
    user        = ForeignKey(User)
    objectType  = models.ForeignKey(ObjectType)

