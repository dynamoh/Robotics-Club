from django.db import models
from accounts.models import Profile

class Events(models.Model):
    """
    all upcoming/ongoing/past events
    """

    title = models.CharField(max_length=500)
    description = models.TextField()
    event_coordinator = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    poster = models.ImageField(upload_to="Events/")
    posted_on = models.DateField(auto_now_add=True)
    event_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Events'
    
    def __str__(self):
        return f'{title}'
