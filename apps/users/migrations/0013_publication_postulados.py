# Generated by Django 2.1.7 on 2019-05-19 23:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_publication_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='postulados',
            field=models.ManyToManyField(related_name='se_postula', to=settings.AUTH_USER_MODEL),
        ),
    ]
