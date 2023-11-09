from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

import datetime 
date = models.DateField('Date', default=datetime.date.today)
time = models.TimeField('Time', default=datetime.time(12, 0))

class Trophy(models.Model):
  name = models.CharField(max_length=100)
  difficulty = models.IntegerField()
  description = models.TextField(max_length=250)
  date = models.TextField(max_length=12)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('trophy-detail', kwargs={'trophy_id': self.id})