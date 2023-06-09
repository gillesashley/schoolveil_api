import random
import secrets
import string

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify


class School(models.Model):
    STATUS_CHOICES = (
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('rejected', 'Rejected')
    )
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    location = models.CharField(max_length=100, default="N/A")
    motto = models.CharField(max_length=100, default="N/A")
    logo = models.ImageField(upload_to='school_logos/', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    slug = models.SlugField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        while School.objects.filter(slug=self.slug).exists():
            # Generate a random 6-character string of lowercase letters
            random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
            self.slug = f"{slugify(self.name)}-{random_string}"
        if not self.pk:
            # Generate a random 16-character alphanumeric password
            self.password = secrets.token_urlsafe(16)
        super().save(*args, **kwargs)

    def clean(self):
        if not self.name:
            raise ValidationError({'name': 'School name is required'})
        if not self.address:
            raise ValidationError({'address': 'School address is required'})
        if not self.phone_number:
            raise ValidationError({'phone_number': 'Phone number is required'})
        if not self.email:
            raise ValidationError({'email': 'Email is required'})
