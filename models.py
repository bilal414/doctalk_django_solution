from django.db import models
from model_utils.models import TimeStampedModel


class Food(TimeStampedModel):
    class Group(models.IntegerChoices):
        MEAT = 1, 'Meat'
        VEGETABLE = 2, 'Vegetable'
        DAIRY = 3, 'Dairy'
        GRAIN = 4, 'Grain'

    name = models.CharField(unique=True, max_length=64)
    group = models.IntegerField(choices=Group.choices)

    class Meta:
        db_table = 'food'
        verbose_name = "Food"
        verbose_name_plural = "Food"


class Profile(models.Model):
    full_name = models.CharField(unique=True, max_length=64)
    dob = models.DateField()
    fav_food = models.ForeignKey(Food, null=True, on_delete=models.SET_NULL())

    class Meta:
        db_table = 'profile'
        verbose_name = "Profile"
        verbose_name_plural = "Profile"
