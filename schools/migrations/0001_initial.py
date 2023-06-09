# Generated by Django 4.1.7 on 2023-03-29 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('location', models.CharField(default='N/A', max_length=100)),
                ('motto', models.CharField(default='N/A', max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='school_logos/')),
                ('status', models.CharField(choices=[('approved', 'Approved'), ('pending', 'Pending'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
