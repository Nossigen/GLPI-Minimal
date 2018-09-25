from django.db import models

class   UserRole        (models.Model):
    name        = models.CharField(max_length = 255)

    def __str__         (self):
        return self.name

class   UserJob         (models.Model):
    name        = models.CharField(max_length = 255)

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
        return (self.forname + " " + self.name)

