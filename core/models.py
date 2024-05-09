from django.db import models

class AgendaModel(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=30, default='')  # Defina o valor padrão aqui

    def __str__(self):
        return self.nome