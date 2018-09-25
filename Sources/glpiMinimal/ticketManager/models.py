from django.db import models

#from userManager.models         import User
from objectManager.models       import Object

class   TicketState     (models.Model):
    name        = models.CharField(max_length = 255)

    def __str__         (self):
        return self.name

class   Ticket          (models.Model):
    ref         = models.UUIDField()
    name        = models.CharField(max_length = 255)

    # Links
    ticketState = models.ForeignKey(TicketState, on_delete = models.CASCADE)
    #creator     = models.ForeignKey(User, on_delete = models.CASCADE)
    ticketObject = models.ForeignKey(Object, on_delete = models.CASCADE)
    # Link to Object

    def __str__         (self):
        return self.name

class   TicketMessage   (models.Model):
    text        = models.TextField()
    dateTime    = models.DateTimeField()

    # Links
    ticket      = models.ForeignKey(Ticket, on_delete = models.CASCADE)
    # Link to User

    def __str__         (self):
        return self.text
