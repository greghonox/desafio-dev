from django.db import models

class transacao_CNAB(models.Model):
    tipo = models.IntegerField(max_length=1)
    data = models.DateField(auto_now_add=True)
    valor = models.FloatField(max_length=10)
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField(auto_now_add=True)
    dono_loja = models.CharField(max_length=14)
    nome_loja = models.TextField(max_length=19)
    
    class Meta:
        ...
    
    def __str__(self): return f"{self.cartao} {self.data} {self.hora} {self.cpf}"

class cargar_arquivo_txt(models.Model):
    nome_arquivo = models.TextField()
    conteudo_arquivo = models.TextField()
    tamanho_arquivo = models.IntegerField()
    data_hora_carga = models.DateTimeField(auto_now_add=True)

    def __str__(self): return f"{self.nome_arquivo} {self.data_hora} {self.tamanho} {self.conteudo[:100]}"