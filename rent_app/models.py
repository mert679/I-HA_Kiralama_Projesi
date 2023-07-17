from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class User(AbstractUser):
    pass


class Iha(models.Model):
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    weight = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    air_time = models.PositiveIntegerField()
    flight_altitude = models.PositiveIntegerField()
    speed = models.IntegerField()
    
    
    def __str__(self):
        return self.model
    
class RentRecord(models.Model):
    user_rent = models.ForeignKey(User, on_delete=models.CASCADE)
    iha = models.ForeignKey(Iha, on_delete=models.CASCADE)
    rental_start_date = models.DateField(default=None, null=True)
    rental_end_date = models.DateField(default=None, null=True)

    def clean(self):
        if self.rental_start_date >= self.rental_end_date:
            raise ValidationError("End time must be greater than start time.")
