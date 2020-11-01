from django.db import models

# Create your models here.
from apps.chapa.models import Chapa


class Votacao(models.Model):
    chapa = models.OneToOneField(
        Chapa,
        on_delete=models.CASCADE,
    )

    votos = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Votações'

    def __str__(self):
        return f'{self.chapa}, Votos: {self.votos}'
