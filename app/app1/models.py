from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Model1(models.Model):
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return self.name
