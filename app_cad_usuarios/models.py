from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    sobrenome = models.TextField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    idade = models.IntegerField()
    endereco = models.TextField(max_length=255)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'