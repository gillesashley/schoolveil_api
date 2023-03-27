from django.db import models
from django.utils.text import slugify

from classes.models import Class
from departments.models import Department
from schools.models import School
from teachers.models import Teacher


class Subject(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_level = models.ForeignKey(Class, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
