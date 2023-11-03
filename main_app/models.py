from django.db import models
from django.urls import reverse

class Trophy(models.Model):
  name = models.CharField(max_length=100)
  difficulty = models.IntegerField()
  description = models.TextField(max_length=250)
  date = models.TextField(max_length=12)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('trophy-detail', kwargs={'trophy_id': self.id})