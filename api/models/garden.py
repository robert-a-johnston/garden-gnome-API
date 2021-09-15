from django.db import models
from django.contrib.auth import get_user_model

class Garden(models.Model):
  # Garden Attributes
  name = models.CharField(max_length=250)
  location = models.CharField(max_length=250)
  notes = models.TextField()
  owner = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE
  )

  def __str__ (self):
    return f"{self.name}, location: {self.locaton}"

  def as_dict(self):
    """Returns dictionary of Garden"""
    return {
      'id': self.id,
      'name': self.name,
      'location': self.location,
      'notes': self.notes
    }