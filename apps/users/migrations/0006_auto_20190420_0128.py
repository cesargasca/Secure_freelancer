# Generated by Django 2.1.7 on 2019-04-20 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190319_0234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='public_key_PATH',
            new_name='public_key',
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='postal_code',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='type_of_user',
            field=models.CharField(choices=[('C', 'Cliente'), ('F', 'Freelancer')], max_length=1),
        ),
    ]
