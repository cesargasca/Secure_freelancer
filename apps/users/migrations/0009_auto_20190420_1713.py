# Generated by Django 2.1.7 on 2019-04-20 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_contry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='contry',
            new_name='country',
        ),
    ]
