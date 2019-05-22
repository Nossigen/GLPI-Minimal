from django.db          import models

import uuid
import datetime

class   UserRole        (models.Model):
    name        = models.CharField(max_length = 255)

    def __str__         (self):
        return self.name

class   UserJob         (models.Model):
    name        = models.CharField(max_length = 255)

    def user_number(self):
        return User.objects.filter(userJob = self).count()

    def __str__         (self):
        return self.name

class   User            (models.Model):
    forname     = models.CharField(max_length = 255)
    name        = models.CharField(max_length = 255)
    email       = models.EmailField(max_length = 255, null = True, blank = True)
    oAuthKey    = models.CharField(max_length = 1024)

    entryDate   = models.DateField(null = True, blank = True)
    outDate     = models.DateField(null = True, blank = True)

    # Links
    userRole    = models.ForeignKey(UserRole, on_delete = models.CASCADE)
    userJob     = models.ForeignKey(UserJob, on_delete = models.CASCADE)

    def __str__         (self):
        if (self.name == '__STOCK__'):
            return ('Stock')
        else:
            return (self.forname + " " + self.name)

##########
# Vendor #
##########

class   CommandState    (models.Model):
    name        = models.CharField(max_length = 255)

    def __str__         (self):
        return self.name

class   Vendor          (models.Model):
    name        = models.CharField(max_length = 255)
    adress      = models.CharField(max_length = 512)
    email       = models.EmailField(null = True, blank = True)
    comment     = models.TextField(null = True, blank = True)

    def __str__         (self):
        return self.name

class   Command         (models.Model):

    ref         = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    reference   = models.CharField(max_length = 255)

    # Links
    commandState        = models.ForeignKey(CommandState, on_delete = models.CASCADE)
    vendor              = models.ForeignKey(Vendor, on_delete = models.CASCADE)

    def __str__         (self):
        return str(self.ref)

class   ObjectType      (models.Model):
    name        = models.CharField(max_length = 255)

    def object_number(self):
        return Object.objects.filter(objectType = self).count()

    def __str__         (self):
        return self.name

class   ObjectDataType        (models.Model):
    name        = models.CharField(max_length = 255)
    s_type      = models.CharField(max_length = 3)
    mendatory   = models.BooleanField()
    visible     = models.BooleanField()

    # Links
    objectType  = models.ForeignKey(ObjectType, on_delete = models.CASCADE,
                                    null = True, blank = True)

    def __str__         (self):
        return self.name

##########
# Object #
##########

class   ObjectState     (models.Model):
    name        = models.CharField(max_length = 255)
    color       = models.CharField(max_length = 7)

    def __str__         (self):
        return self.name

class   Object          (models.Model):
    ref         = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name        = models.CharField(max_length = 255)
    depth       = models.IntegerField()

    # Links
    objectIn    = models.ManyToManyField('self', blank = True)
    user        = models.ForeignKey(User, on_delete = models.CASCADE)
    command     = models.ForeignKey(Command, on_delete = models.CASCADE,
                                    null = True, blank = True)
    objectType  = models.ForeignKey(ObjectType, on_delete = models.CASCADE)

    def last_history(self):
        histories = ObjectHistory.objects.filter(objectShown = self)
        last_state = 0

        print('')
        print('object')
        print(self.name)
        for history in histories:
            print('current history')
            print(history.objectState.name)
            print('date history')
            print(history.date)
            if (last_state != 0):
                print('date last_state')
                print(last_state.date)
            if (last_state == 0):
                print('init last state:')
                print(history.objectState.name)
                last_state = history
            elif (history.date > last_state.date):
                print('new last state')
                print(history.objectState.name)
                last_state = history

        return (last_state)

    def __str__         (self):
        return self.name

class   ObjectData            (models.Model):
    value       = models.TextField(null = True, blank = True)

    # Links
    item                = models.ForeignKey(Object, on_delete = models.CASCADE)
    objectDataType      = models.ForeignKey(ObjectDataType, on_delete = models.CASCADE)

    def __str__         (self):
        return self.value

class   ObjectHistory   (models.Model):
    ref         = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    comment     = models.TextField(null = True, blank = True)
    date        = models.DateField(default = datetime.date.today)
    position    = models.CharField(max_length = 512)

# Links
    objectState = models.ForeignKey(ObjectState, on_delete = models.CASCADE,
                                    null = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    objectShown = models.ForeignKey(Object, on_delete = models.CASCADE)

    def __str__         (self):
        return str(self.date) + ' - ' + str(self.ref)

# Object value

##########
# Ticket #
##########

class   TicketState     (models.Model):
    name        = models.CharField(max_length = 255)

    def __str__         (self):
        return self.name

class   Ticket          (models.Model):
    ref         = models.UUIDField()
    name        = models.CharField(max_length = 255)

    # Links
    ticketState     = models.ForeignKey(TicketState, on_delete = models.CASCADE)
    creator         = models.ForeignKey(User, on_delete = models.CASCADE)
    ticketObject    = models.ForeignKey(Object, on_delete = models.CASCADE)
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
