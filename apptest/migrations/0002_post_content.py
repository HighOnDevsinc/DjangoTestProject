# Generated by Django 5.0.7 on 2024-07-10 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='Nothing to show'),
            preserve_default=False,
        ),
    ]
