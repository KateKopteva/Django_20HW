from django.db import models
from django.urls import reverse

class Employees(models.Model):
    id = models.IntegerField
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    proffession = models.CharField(max_length=400)

    def get_absolute_url(self):
        return reverse('addpage', kwargs={'post_id':self.pk})
