from django.db import models

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=20)
    Mail=models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=12)
    passwd=models.CharField(max_length=20)
    def __str__(self):
        return self.Name
    
class Room(models.Model):
    roomno=models.SmallIntegerField(max_length=5)
    room_type=models.CharField(max_length=10)
    capacity=models.SmallIntegerField(max_length=1)
    rate=models.SmallIntegerField(max_length=4)
    def __str__(self):
        return self.room_type

class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    guest=models.SmallIntegerField(max_length=2)
    chekindate=models.DateField('Checkin date')
    chekoutdate=models.DateField('Checkout date')


