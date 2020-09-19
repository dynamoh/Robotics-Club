from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, date

from accounts.models import Profile
from RoboticsClub.globals import POSTS


def current_year():
    return date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Team(models.Model):
    """
    Data of all Team members till date.
    NOTE: current team members will be fetched by most recent date
    """

    profile_id = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="teamMember")
    post = models.CharField(max_length=750, choices=POSTS)

    linkedIn = models.URLField(max_length=1200)
    facebook = models.URLField(max_length=1200)
    twitter = models.URLField(max_length=1200)

    appointed_for = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(2012), max_value_current_year])

    class Meta:
        verbose_name_plural = 'Team Members'
    
    def __str__(self):
        return f'{self.name} - {self.email}'

