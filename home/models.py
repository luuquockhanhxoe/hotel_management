from typing import ClassVar
from django.db import models
from django.db.models.base import Model

class Category_Hoel(models.Model):
    CategoryCode = models.CharField(max_length=20)
    CategoryName = models.CharField(max_length=50)
    # CategoryDescription = models.CharField(max_length=500, default='')
    # PictureHotel = models.ImageField(upload_to='Category_picture')

    def __str__(self):
        return self.CategoryName

class Room_Info(models.Model):
    RoomCode = models.CharField(max_length=20)
    KindOfRoom = models.CharField(max_length=100)
    Price = models.IntegerField()
    Status = models.CharField(max_length=100)
    RoomTel = models.CharField(max_length=12)
    CategoryCode = models.ForeignKey(Category_Hoel, on_delete=models.CASCADE)


    def __str__(self):
        return self.KindOfRoom

class Customer_Info(models.Model):
    CustomerCode = models.CharField(max_length=20)
    FullName = models.CharField(max_length=100)
    CustomerTel = models.CharField(max_length=12)
    CCCD = models.CharField(max_length=12)

    def __str__(self):
        return self.FullName

class Room_Use(models.Model):
    CustomerCode = models.ForeignKey(Customer_Info, on_delete=models.CASCADE)
    RoomCode = models.ForeignKey(Room_Info, on_delete=models.CASCADE)

    def __str__(self):
        return self.RoomCode

class Service(models.Model):
    ServiceCode = models.CharField(max_length=20)
    ServiceName = models.CharField(max_length=50)
    UnitPrice = models.IntegerField(default=0)

    def __str__(self):
        return self.ServiceName

class Book_Room(models.Model):
    CustomerCode = models.ForeignKey(Customer_Info, on_delete=models.CASCADE)
    RoomCode = models.ForeignKey(Room_Info, on_delete=models.CASCADE)
    ReceivedDate = models.DateField()

    def __str__(self):
        return self.ReceivedDate
