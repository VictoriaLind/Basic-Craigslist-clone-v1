# Generated by Django 4.1.7 on 2023-02-27 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
