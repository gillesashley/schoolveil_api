from django.contrib import admin

from schools.models import School


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'email', 'status', 'slug')
    list_filter = ('status',)
    search_fields = ('name', 'address', 'phone_number', 'email')


admin.site.register(School, SchoolAdmin)

# Register your models here.
