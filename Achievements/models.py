from django.db import models
from django.utils import timezone

class Achievements(models.Model):
    """
    Achievemnts of members of Robotics club.
    NOTE: only recent achievements will be showcased on homepage 
    """

    event = models.CharField(max_length=450)
    description = models.TextField()
    achieved_on = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='Achievements/')

    class Meta:
        verbose_name_plural = 'Achievements'
    
    def __str__(self):
        return f'{event}'
