from django.db import models

# Create your models here.
class User(models.Model):
    firstname=models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=120)
    username=models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.username

class Account(models.Model):
    account_number=models.CharField(max_length=12,unique="True")
    account_type=models.CharField(max_length=12)
    username=models.CharField(max_length=50)
    balance=models.FloatField()

    def __str__(self):
        return self.accountnumber


class Login(models.Model):
    username=models.CharField(max_length=120,unique=True)
    password = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.username