from django.db import models

from userManager.models import User
from objectManager.models import Object

class   ObjectState     (models.Model):
    name        = models.CharField(max_length = 255)

    def __str__         (self):
        return self.name

class   ObjectHistory   (models.Model):
    ref         = models.UUIDField(primary_key = True)
    comment     = models.TextField(null = True, blank = True)
    date        = models.DateField()
    position    = models.CharField(max_length = 512)

    # Links
    objectState = models.ForeignKey(ObjectState, on_delete = models.CASCADE)

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    objectShown = models.ForeignKey(Object, on_delete = models.CASCADE)
    #admin = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__         (self):
        return str(self.ref)

