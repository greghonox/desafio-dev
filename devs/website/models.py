from django.db import models
from django.core.validators import MaxValueValidator


class Transacao_CNAB(models.Model):
    tipo = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(9)])
    data = models.DateField(auto_now_add=True)
    valor = models.FloatField(max_length=10)
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField(auto_now_add=True)
    dono_loja = models.CharField(max_length=14)
    nome_loja = models.CharField(max_length=19)

    class Meta:
        ...

    def __str__(self):
        return f"{self.cartao} {self.data} {self.hora} {self.cpf}"


class Arquivo_txt(models.Model):
    conteudo = models.TextField(blank=False)
    data_hora_carga = models.DateTimeField(auto_now_add=True)
    url = models.FileField(verbose_name="Arquivo da Transação")

    def __str__(self):
        return f"{self.url} {self.data_hora_carga} {self.conteudo[:100]}"
