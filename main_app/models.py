from django.db import models


class Trophy(models.Model):
  name = models.CharField(max_length=100)
  difficulty = models.IntegerField()
  description = models.TextField(max_length=250)
  date = models.TextField(max_length=12)

  def __str__(self):
    return self.name