# Generated by Django 2.1.7 on 2019-06-05 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20190604_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='publication',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publication2', to='users.Publication'),
        ),
    ]
