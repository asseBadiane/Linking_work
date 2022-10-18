# Generated by Django 4.1 on 2022-10-14 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import job.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('photo', models.ImageField(upload_to='')),
                ('metier', models.CharField(max_length=50, verbose_name=job.models.Metier)),
                ('bio', models.CharField(max_length=200)),
                ('adress_home', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=9)),
                ('etoile', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('ouvrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ouvrier', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Metier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('metier', models.CharField(max_length=50, verbose_name='Ton Métier')),
                ('description', models.CharField(max_length=100, null=True)),
                ('zone_de_deplacement', models.CharField(choices=[('DAKAR', 'DAKAR'), ('THEIS', 'THEIS'), ('LOUGA', 'LOUGA')], max_length=30)),
                ('jour_de_travaille', models.CharField(choices=[('LUNDI', 'LUNDI'), ('MARDI', 'MARDI'), ('MERCREDI', 'MERCREDI'), ('JEUDI', 'JEUDI'), ('VENDREDI', 'VENDREDI'), ('DIMANCHE', 'DIMANCHE'), ('DIMANCHE', 'DIMANCHE')], max_length=30)),
                ('heure_de_travaille', models.CharField(max_length=30)),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='worker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]