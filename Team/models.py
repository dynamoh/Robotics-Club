from django.db import models

from accounts.models import Profile
from RoboticsClub.globals import POSTS

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

    appointed_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Team Members'
    
    def __str__(self):
        return f'{self.name} - {self.email}'

