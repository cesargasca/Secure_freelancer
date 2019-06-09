# Generated by Django 2.1.7 on 2019-05-20 00:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_publication_postulados'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postulados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('rechazado', 'rechazado'), ('aceptado', 'aceptado'), ('en revision', 'en revision')], max_length=25)),
            ],
        ),
      
        migrations.AddField(
            model_name='postulados',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publication', to='users.Publication'),
        ),
        migrations.AddField(
            model_name='postulados',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]