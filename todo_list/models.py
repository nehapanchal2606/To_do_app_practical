from django.db import models


# create model for register data
class Profile(models.Model):
    firstame = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=8)
    contact = models.CharField(max_length=12)

    def __str__(self):
        return self.firstname
    
# create model add to do  list
class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item
    