# Generated by Django 5.0.6 on 2024-10-06 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast_epsiode', '0002_remove_podcastepisodepremium_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcastepisodepremium',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/podcast/'),
        ),
    ]
