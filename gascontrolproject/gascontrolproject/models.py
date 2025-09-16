from django.db import models

# Aqui estou criando os modelos

class Condominio(models.Model):
    nome = models.CharField(max_length=20)
    local = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Torres(models.Model):
    identificacao = models.CharField(max_length=10, default='Bloco X')
    numero = models.CharField(max_length=10)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='torres')

    def __str__(self):
        return (f"{self.numero} - {self.identificacao}")
    
class Apartamento(models.Model):
    numero = models.CharField(max_length=10)
    torre = models.ForeignKey(Torres, on_delete=models.CASCADE, related_name='apartamentos')
    
    def __str__(self):
        return (f"Apto {self.numero} - {self.torres.identificacao}")
    
class Pessoa(models.Model):
    TIPO_ESCOLHA=[
        ('DONO', 'Dono'),
        ('INQUILINO', 'Inquilino'),
        ('MORADOR', 'Morador'),
    ]
    
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=10, choices=TIPO_ESCOLHA)
    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE, related_name='pessoas')
    
    def __str__(self):
        return (f"{self.nome} ({self.get_tipo_display()})")
    

class Hidrometro(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    apartamento = models.OneToOneField(Apartamento, on_delete=models.CASCADE, related_name='hidrometro')
    
    def __str__(self):
        return f"Hidrômetro {self.codigo} - Apto {self.apartamento.numero}"
    
class Leitura(models.Model):
    PERIODICIDADE_CHOICES = [
        ('SEMANAL', 'Semanal'),
        ('MENSAL', 'Mensal'),
        ('BIMESTRAL', 'Bimestral'),
    ]
    
    hidrometro = models.ForeignKey(Hidrometro, on_delete=models.CASCADE, related_name='leituras')
    data_leitura = models.DateField()
    consumo_m3 = models.DecimalField(max_digits=10, decimal_places=2)
    periodicidade = models.CharField(max_length=10, choices=PERIODICIDADE_CHOICES, default='MENSAL')
    
    class Meta:
        unique_together = ['hidrometro', 'data_leitura']
    
    def __str__(self):
        return f"Leitura {self.hidrometro.codigo} - {self.data_leitura}"