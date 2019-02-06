from django.db import models

# Create your models here.
class User_bal(models.Model):
    acc_no = models.IntegerField(max_length=5,)
    Username = models.CharField(max_length=100,unique=True)
    Password = models.CharField(max_length=50)
    Balance = models.CharField(max_length=10,default=0)
    def __str__(self):
        return self.Name

