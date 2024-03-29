from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):

    username   = models.CharField(max_length = 250, primary_key = True)
    password   = models.CharField(max_length = 250)
    role       = models.CharField(max_length = 250, null = True)
    last_visit = models.DateTimeField(null = True, blank = True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    def __str__(self):
        return self.username

class City(models.Model):
    name = models.CharField(max_length = 100, null = True)

    def __str__(self):
        return self.name 

class Address(models.Model):
    address     = models.CharField(max_length = 300, null = True)
    postal_code = models.CharField(max_length = 10, null = True) 
    city        = models.ForeignKey(City, on_delete = models.CASCADE)

    def __str__(self):

        return self.city.name + ' ' + self.address

class Customer(models.Model):

    first_name = models.CharField(max_length = 100, null = True)
    last_name  = models.CharField(max_length = 100, null = True)
    nat_code   = models.CharField(max_length = 100, null = True)
    #account    = models.OneToOneField(CustomUser)

    def __str__(self):

        return self.first_name + ' ' + self.last_name

class Platform(models.Model):
    name = models.CharField(max_length = 30, null = True)

    def __str__(self):
        return self.name

class G_Category(models.Model):
    c_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.c_name

class Game(models.Model):
    name    = models.CharField(max_length = 100)
    describ = models.TextField()
    gameCat = models.ForeignKey(G_Category, on_delete = models.CASCADE)
    gamePlt = models.ForeignKey(Platform, on_delete = models.CASCADE)
    price   = models.IntegerField(default = 0)
    picture = models.ImageField(upload_to = 'pic_folder/')

    def __str__(self):

        return self.name + ' ' + self.gamePlt.name

class GameOrder(models.Model):
    customer   = models.ForeignKey(Customer, on_delete = models.CASCADE)
    gameEntity = models.ForeignKey(Game, on_delete = models.CASCADE)

    def __str__(self):

        return str(self.id) 

class GameDelivery(models.Model):
    order   = models.ForeignKey(GameOrder, on_delete = models.CASCADE)
    address = models.ForeignKey(Address, on_delete = models.CASCADE)

    def __str__(self):

        return str(self.id)

class A_Category(models.Model):

    name = models.CharField(max_length = 100, null = True)

    def __str__(self):

        return self.name

class Accessory(models.Model):
    name         = models.CharField(max_length = 100)
    describ      = models.TextField()
    accessoryCat = models.ForeignKey(A_Category, on_delete = models.CASCADE)
    accessoryPlt = models.ForeignKey(Platform, on_delete = models.CASCADE)
    price        = models.IntegerField(default = 0)
    picture      = models.ImageField(upload_to = 'pic_folder/')

    def __str__(self):

        return self.name + ' ' + self.accessoryPlt.name

class AccessoryOrder(models.Model):
    customer        = models.ForeignKey(Customer, on_delete = models.CASCADE)
    accessoryEntity = models.ForeignKey(Accessory, on_delete = models.CASCADE)

    def __str__(self):

        return str(self.id) 

class AccessoryDelivery(models.Model):
    order   = models.ForeignKey(AccessoryOrder, on_delete = models.CASCADE)
    address = models.ForeignKey(Address, on_delete = models.CASCADE)