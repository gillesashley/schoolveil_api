from django.contrib import admin

# Register your models here.
from classes.models import Class


class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'school', 'teacher', 'department', 'created_at', 'updated_at')
    list_filter = ('department',)
    search_fields = ('name', 'teacher',)


admin.site.register(Class, ClassAdmin)
