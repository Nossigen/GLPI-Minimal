from django.db import models

class   CommandState    (models.Model):
    name        = models.CharField(max_length = 255)

    def __str__         (self):
        return self.name

class   Vendor          (models.Model):
    name        = models.CharField(max_length = 255)
    adress      = models.CharField(max_length = 512)
    email       = models.EmailField(null = True)
    comment     = models.TextField(null = True)

    def __str__         (self):
        return self.name

class   Command         (models.Model):
    ref         = models.UUIDField(primary_key = True)

    # Links
    commandState        = models.ForeignKey(CommandState, on_delete = models.CASCADE)
    vendor              = models.ForeignKey(Vendor, on_delete = models.CASCADE)

    def __str__         (self):
        return str(self.ref)

