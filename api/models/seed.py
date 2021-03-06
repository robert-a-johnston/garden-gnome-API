from api.models.garden import Garden
from django.db import models
from django.contrib.auth import get_user_model
from .garden import Garden

# seed model
class Seed(models.Model):
  # seed attributes
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100, blank=True)
  season = models.CharField(max_length=100, blank=True)
  light = models.CharField(max_length=100, blank=True)
  favorite = models.BooleanField()
  planted = models.BooleanField()
  number = models.CharField(max_length=100, blank=True)
  notes = models.TextField(blank=True)
  owner = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE
  )

  # shows up in admin screen in browser
  def __str__(self):
    # returns info string
    return f"{self.name}, {self.type}, {self.number}"

  def as_dict(self):
    """Returns dictionary of Seed"""
    return {
      'id': self.id,
      'name': self.name,
      'type': self.type,
      'light': self.light,
      'favorite': self.favorite,
      'number': self.number,
      'notes': self.notes,
    }
