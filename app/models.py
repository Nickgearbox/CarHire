from django.db import models
from django.utils import timezone

class Registrant(models.Model):
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=255)  # NOTE: Use Django's User model in production for better security
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Prefer not to say')])

    def __str__(self):
        return self.username
    
class Contact(models.Model):
    name =models.CharField(max_length=50)
    email =models.CharField(max_length=50)
    message =models.CharField(max_length=50)
    
    def __str__(self):
        return  f"{self.name} sent you a message"
    
class CarImage(models.Model):
    id = models.AutoField(primary_key=True)
    image=models.FileField(upload_to='static/img')
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100, default="No description provided")
    model = models.CharField(max_length=50)
    gear=models.CharField(max_length=50)
    km=models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    
class Bookings(models.Model):
    p_location = models.CharField(max_length=50,default='Karen')
    num_adult = models.PositiveIntegerField(default=1)
    num_children = models.PositiveIntegerField(default=1)
    car= models.CharField(max_length=50,)
    
    def __str__(self) :
        return f'You have booked {self.car}'

    
    
class Area(models.Model):
    pickup = models.CharField(max_length=50)
    dropdown = models.CharField(max_length=50)
    num_child = models.CharField(max_length=50)
    num_adult = models.CharField(max_length=50)
    
    def __str__(self):
        return self.pickup
