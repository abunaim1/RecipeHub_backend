# Generated by Django 5.0.6 on 2024-09-27 03:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatAPI', '0003_chatgroup_groupmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmessage',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chatAPI.profile'),
        ),
    ]
