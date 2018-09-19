from django.db import models

from userManager.models         import User
from vendorManager.models       import Command

# Object definition
class   ObjectType      (models.Model):
    name        = models.CharField(max_length = 255)

    # Links
    objectIn    = models.ForeignKey('self', on_delete = models.CASCADE)

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
    ref         = models.UUIDField(primary_key = True)
    name        = models.CharField(max_length = 255)

    # Links
    objectIn    = models.ForeignKey('self', on_delete = models.CASCADE)
    user        = models.ForeignKey(User, on_delete = models.CASCADE)
    command     = models.ForeignKey(Command, on_delete = models.CASCADE)
    objectType  = models.ForeignKey(ObjectType, on_delete = models.CASCADE)

    def __str__         (self):
        return self.name

class   ObjectData            (models.Model):
    value       = models.TextField(null = True)

    # Links
    item                = models.ForeignKey(Object, on_delete = models.CASCADE)
    objectDataType      = models.ForeignKey(ObjectDataType, on_delete = models.CASCADE)

    def __str__         (self):
        return self.value
