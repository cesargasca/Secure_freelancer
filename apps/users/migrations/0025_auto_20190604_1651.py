# Generated by Django 2.1.7 on 2019-06-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_contract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='client_signature',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='freelancer_signature',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
