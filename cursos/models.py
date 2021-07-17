from django.db import models

# Create your models here.
class Curso(models.Model):
    nome= models.CharField(max_length= 250)
    tipo= models.CharField(max_length= 150)
    preço= models.CharField(max_length= 10)

    def __str__(self):
        return self.nome
    