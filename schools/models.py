import random
import secrets
import string

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class School(models.Model):
    STATUS_CHOICES = (
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('rejected', 'Rejected')
    )
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    location = models.CharField(max_length=100, default="N/A")
    logo = models.ImageField(upload_to='school_logos/', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    slug = models.SlugField(unique=True, null=True, blank=True)
    temp_password = models.CharField(max_length=128, null=True, blank=True)
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
            self.temp_password = secrets.token_urlsafe(16)
        super().save(*args, **kwargs)
