from django.db import models


class Contacts(models.Model):
    """
    all the data coming from contact us form.
    NOTE: Team members will receive mail about queries.
    """

    first_name = models.CharField(max_length=350)
    last_name = models.CharField(max_length=350)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    subject = models.CharField(max_length=1200)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return f'{first_name} {last_name}'

class Gallery(models.Model):
    """
    images/videos related to all Robotics club events. 
    NOTE: files will be seggregated by type while displaying.
    """

    file = models.FileField(upload_to='Gallery/')
    caption = models.CharField(max_length=1500)
    uploaded_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return f'{self.caption[:50]}'