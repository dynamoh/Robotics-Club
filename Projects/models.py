from django.db import models
from accounts.models import Profile

class Projects(models.Model):
    """
    Data of all projects created by robotics club till date.
    NOTE: only selected projects will be showcased.
    """

    tile = models.CharField(max_length=300)
    description = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    team_members = models.ManyToManyField(Profile, blank=True, related_name="projectMembers")
    project_lead = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True )


def project_file_upload_path(instance, filename):
    return f'Projects/{instance.project_id.title}/{filename}'

class ProjectFiles(models.Model):
    """
    All files related to projects including images, videos, docs, pdf
    NOTE: files will be seggregated by type while displaying.
    """

    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name="profectFiles")
    file = models.FileField(upload_to=project_file_upload_path)
    uploaded_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Project Files'

    def __str__(self):
        return f'{project_id.title}'


