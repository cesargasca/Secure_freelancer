# Generated by Django 2.1.7 on 2019-03-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='need_email', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='need_usename', max_length=50, unique=True),
        ),
    ]