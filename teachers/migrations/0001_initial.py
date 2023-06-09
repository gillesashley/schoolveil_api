# Generated by Django 4.1.7 on 2023-03-29 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('qualification', models.CharField(max_length=100)),
                ('teacher_type', models.CharField(choices=[('CT', 'Class Teacher'), ('ST', 'Subject Teacher')], max_length=3)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.school')),
            ],
        ),
    ]
