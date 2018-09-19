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
    OAuthKey    = models.CharField(max_length = 1024)

    # Links
    userRole    = models.ForeignKey(UserRole, on_delete = models.CASCADE)
    userJob     = models.ForeignKey(UserJob, on_delete = models.CASCADE)

    def __str__         (self):
        return self.forname + " " + self.name

