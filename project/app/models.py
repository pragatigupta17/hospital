from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    Specilastion=models.CharField(max_length=100)
    image=models.ImageField(upload_to = 'image/')
    password=models.CharField(max_length=50)

class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    occupation=models.CharField(max_length=100)
    image=models.ImageField(upload_to = 'image/')
    password=models.CharField(max_length=50)







class Appoiment(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    
    DEPARTMENT_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Orthopedics', 'Orthopedics'),
        ('General', 'General')
    ]
    
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    symptoms = models.TextField()
    date = models.DateField()
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Appointment for {self.name} on {self.date} at {self.time}"
    



class Product(models.Model):
    amount = models.CharField(max_length=100 , blank=True)
    order_id = models.CharField(max_length=1000 )
    razorpay_payment_id = models.CharField(max_length=1000 ,blank=True)
    paid = models.BooleanField(default=False)
    def __str__(self):
        return self.name