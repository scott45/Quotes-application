from django.db import models
from django.contrib.auth.models import User

# my quotes model


class Quote(models.Model):
    title = models.CharField("Quote", max_length=200)
    submitter = models.ForeignKey(User)
    submitted_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "quotes"
