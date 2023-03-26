import random
import string

from django.db import models
from django.utils.text import slugify

from classes.models import Class
from schools.models import School


class Teacher(models.Model):
    TEACHER_TYPE_CHOICES = (
        ('CT', 'Class Teacher'),
        ('ST', 'Subject Teacher'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    teacher_type = models.CharField(max_length=2, choices=TEACHER_TYPE_CHOICES, default='CT')
    slug = models.SlugField(unique=True, null=True, blank=True)
    classroom = models.ForeignKey(
        Class, on_delete=models.CASCADE, limit_choices_to={'school': school}
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name} {self.last_name}")
        while Teacher.objects.filter(slug=self.slug).exists():
            # Generate a random 6-character string of lowercase letters
            random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
            self.slug = f"{slugify(f'{self.first_name} {self.last_name}')}-{random_string}"
        super().save(*args, **kwargs)
