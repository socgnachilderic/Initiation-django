from django.db import models
from datetime import datetime

# Create your models here.

class Tutoriel(models.Model):
    tutoriel_titre = models.CharField(max_length=200)
    tutoriel_contenu = models.TextField()
    tutoriel_publier = models.DateTimeField("date publiée", default=datetime.now())

    def __str__(self):
        return self.tutoriel_titre

