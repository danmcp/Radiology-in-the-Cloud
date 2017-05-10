import datetime
from django.utils import timezone
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

class ImageProcessingRequest(models.Model):
    created = models.DateTimeField(default=datetime.datetime.now)
    patientid = models.CharField(max_length=100)
    jobtype = models.CharField(max_length=100)
    jobstatus = models.CharField(max_length=100)

    class Meta:
        ordering = ('created',)