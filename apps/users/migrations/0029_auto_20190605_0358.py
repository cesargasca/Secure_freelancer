# Generated by Django 2.1.7 on 2019-06-05 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20190605_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='private_key',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
