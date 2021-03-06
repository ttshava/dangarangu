# Generated by Django 3.2.8 on 2021-10-21 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cattle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('stud', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1)),
                ('dob', models.DateField()),
                ('status', models.CharField(choices=[('A', 'Active'), ('S', 'Sold'), ('D', 'Dead')], max_length=1)),
                ('breed', models.CharField(choices=[('B', 'Boran Angus'), ('A', 'Ankole'), ('M', 'Mashona'), ('N', 'Brahman'), ('D', 'Dexter'), ('F', 'Beefmaster'), ('H', 'Hereford'), ('R', 'Red Poll'), ('D', 'Afrikaner'), ('T', 'Tuli')], max_length=1)),
                ('cattle_colour', models.CharField(max_length=200)),
                ('horn', models.CharField(choices=[('H', 'Horned'), ('P', 'Polled'), ('S', 'Very short'), ('D', 'Dehoned')], max_length=1)),
                ('conception', models.CharField(choices=[('N', 'Natural'), ('A', 'Artificial'), ('E', 'Embryo')], max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'order_with_respect_to': 'user',
            },
        ),
    ]
