from django.contrib import admin

from .models import Arquivo_txt, Transacao_CNAB
from .forms import ArquivosForms, TransacoesForms


class ArquivoAdmin(admin.ModelAdmin):
    list_display = ["id", "url", "data_hora_carga"]
    list_filter = list_display
    list_per_page = 50
    form = ArquivosForms


class TransacaoAdmin(admin.ModelAdmin):
    list_display = ["tipo", "data", "valor", "cpf", "cartao"]
    list_filter = list_display
    list_per_page = 50
    form = TransacoesForms


admin.site.register(Arquivo_txt, ArquivoAdmin)
admin.site.register(Transacao_CNAB, TransacaoAdmin)
