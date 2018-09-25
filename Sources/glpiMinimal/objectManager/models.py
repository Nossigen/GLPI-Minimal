from django.db import models

import uuid

#from userManager.models         import User
#from vendorManager.models       import Command

# Object definition
class   ObjectType      (models.Model):
    name        = models.CharField(max_length = 255)

    def __str__         (self):
        return self.name

class   ObjectDataType        (models.Model):
    name        = models.CharField(max_length = 255)
    s_type      = models.CharField(max_length = 3)
    mendatory   = models.BooleanField()
    visible     = models.BooleanField()

    # Links
    objectType  = models.ForeignKey(ObjectType, on_delete = models.CASCADE)

    def __str__         (self):
        return self.name

# Object value
class   Object          (models.Model):
    ref         = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name        = models.CharField(max_length = 255)
    depth       = models.IntegerField()

    # Links
    objectIn    = models.ManyToManyField('self', blank = True)
    #user        = models.ForeignKey(User, on_delete = models.CASCADE)
    #command     = models.ForeignKey(Command, on_delete = models.CASCADE,
    #null = True, blank = True)
    objectType  = models.ForeignKey(ObjectType, on_delete = models.CASCADE)

    def __str__         (self):
        return self.objectType.name

class   ObjectData            (models.Model):
    value       = models.TextField(null = True, blank = True)

    # Links
    item                = models.ForeignKey(Object, on_delete = models.CASCADE)
    objectDataType      = models.ForeignKey(ObjectDataType, on_delete = models.CASCADE)

    def __str__         (self):
        return self.value
