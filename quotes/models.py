from django.db import models
from django.contrib.auth.models import User

# my quotes model

class Quote(models.Model):
    title = models.CharField("Quote", max_length=100)
    submitter = models.ForeignKey(User)
    submitted_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)


