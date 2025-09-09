from django.db import models

class Condominio(models.Model):
    nome = models.CharField(max_length=20, default='Condominio Sorgatto')
    local = models.CharField(max_length=50, default='Tatuapé')

    def __str__(self):
        return self.nome


class Torres(models.Model):
    nome = models.CharField(max_length=10, default='Bloco X')

    def __str__(self):
        return self.lugar
    
