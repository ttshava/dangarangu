from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cattle(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    stud_choices = (
        ('Y', 'Yes',),
        ('N', 'No',),
    )
    stud = models.CharField(
        max_length=1,
        choices=stud_choices,
    )

    sex_choices = (
        ('F', 'Female',),
        ('M', 'Male',),

    )
    sex = models.CharField(
        max_length=1,
        choices=sex_choices,
    )
    dob = models.DateField()

    status_choices = (
        ('A', 'Active',),
        ('S', 'Sold',),
        ('D', 'Dead',),
    )
    status = models.CharField(
        max_length=1,
        choices=status_choices,
    )

    breed_choices = (
        ('B', 'Boran Angus',),
        ('A', 'Ankole',),
        ('M', 'Mashona',),
        ('N', 'Brahman',),
        ('D', 'Dexter',),
        ('F', 'Beefmaster',),
        ('H', 'Hereford',),
        ('R', 'Red Poll',),
        ('D', 'Afrikaner',),
        ('T', 'Tuli',),
    )
    breed = models.CharField(
        max_length=1,
        choices=breed_choices,
    )

    cattle_colour = models.CharField(max_length=200)

    horn_choices = (
        ('H', 'Horned',),
        ('P', 'Polled',),
        ('S', 'Very short',),
        ('D', 'Dehoned',),
    )
    horn = models.CharField(
        max_length=1,
        choices=horn_choices,
    )

    conception_choices = (
        ('N', 'Natural',),
        ('A', 'Artificial',),
        ('E', 'Embryo',),

    )
    conception = models.CharField(
        max_length=1,
        choices=conception_choices,
    )

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        order_with_respect_to = 'user'
