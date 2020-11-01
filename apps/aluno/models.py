from django.db import models


# Create your models here.


class Aluno(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    matricula = models.CharField(max_length=10, unique=True)
    ja_votou = models.BooleanField(default=False)


    def __str__(self):
        return 'Votou' if self.ja_votou else 'Não votou'
