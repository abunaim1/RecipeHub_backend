# Generated by Django 5.0.6 on 2024-09-28 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='image',
        ),
        migrations.AddField(
            model_name='recipe',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='uploads/kitchen/'),
        ),
    ]
