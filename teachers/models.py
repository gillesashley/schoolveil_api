from django.db import models

from departments.models import Department
from schools.models import School


class Teacher(models.Model):
    TEACHER_TYPE_CHOICES = (
        ('CT', 'Class Teacher',),
        ('ST', 'Subject Teacher',),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    dob = models.DateField("Date of Birth")
    qualification = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    teacher_type = models.CharField(max_length=3, choices=TEACHER_TYPE_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
