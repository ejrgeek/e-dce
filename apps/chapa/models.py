from django.db import models

# Create your models here.


def upload_foto(instance, filename):
    return f'foto/{filename}'


class Chapa(models.Model):
    nome = models.CharField(max_length=255)
    numero = models.PositiveIntegerField()
    foto = models.ImageField(upload_to=upload_foto)

    def __str__(self):
        return f'{self.nome}, Número: {self.numero}'
