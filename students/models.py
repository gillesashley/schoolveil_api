from django.db import models
from classes.models import Class
from schools.models import School


class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES)
    guardian = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
