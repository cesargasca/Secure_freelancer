# Generated by Django 2.1.7 on 2019-03-19 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190319_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]