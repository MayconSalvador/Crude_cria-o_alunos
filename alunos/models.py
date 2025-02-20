from django.db import models

class Alunos(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    data_matricula = models.DateField()
    ativo = models.BooleanField()
    plano_aula = models.TextField()
    
    def __str__(self):
        return self.nome