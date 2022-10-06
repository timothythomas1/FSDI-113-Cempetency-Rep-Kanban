from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name

# Now create a custom migration for status to communicate to. 
# We are not putting this into the Status class due to later maintainability concerns. (Refactoring?)


class Issue(models.Model):
    title = models.CharField(max_length=256)
    summary = models.CharField(max_length=512)
    description = models.TextField()
    status = models.ForeignKey(
        Status, 
        on_delete=models.CASCADE
    )
    requester = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

def __str__(self):
    return self.title

def get_absolute_url(self):
    return reverse('issue_detail', args=[self.id])
