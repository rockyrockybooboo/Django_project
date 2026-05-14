from django.db import models

# Create your models here.
class Membar(models.Model):
  name = models.CharField(max_length=100)
  age = models.CharField(max_length=3)
  email = models.EmailField(max_length=150)
  passwd = models.CharField(max_length=100)

  def __str__(self):
    return f'{self.id} {self.name}'
  