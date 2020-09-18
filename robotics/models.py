from django.db import models
from RoboticsClub.globals import POSTS

class Team(models.Model):
    """
    list of all coordinators till date.
    NOTE: current coordinator will be fetched by most recent date
    """

    name = models.CharField(max_length=350)
    post = models.CharField(max_length=750, choices=POSTS)

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    
    phone = models.CharField(max_length=10)
    avatar = models.ImageField(upload_to='Coordinators/')

    linkedIn = models.URLField(max_length=1200)
    facebook = models.URLField(max_length=1200)
    twitter = models.URLField(max_length=1200)

    appointed_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Team Members'
    
    def __str__(self):
        return f'{self.name} - {self.email}'

