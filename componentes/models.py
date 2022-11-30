from django.db import models
from django.conf import settings
# ...code

# Create your models here.
class Componente(models.Model):
    name= models.TextField()
    semestre = models.TextField(blank=True)
