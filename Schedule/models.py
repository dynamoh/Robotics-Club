from django.db import models
from accounts.models import Profile

class Schedule(models.Model):
    """
    schedule for club sessions
    NOTE: It will be only visible to club members ( registered users ) 
    """

    title = models.CharField(max_length=500)
    agenda = models.TextField()
    location = models.CharField(max_length=500)
    scheduled_for = models.DateField()
    scheduled_on = models.DateField(auto_now_add=True)
    host = models.ManyToManyField(Profile, blank=True, related_name="sessionHosts")

    class Meta:
        verbose_name_plural = "Schedule"

    def __str__(self):
        return f'{self.title}'
