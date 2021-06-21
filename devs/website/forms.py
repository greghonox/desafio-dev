from django import forms

from .models import Arquivo_txt, Transacao_CNAB


class ArquivosForms(forms.ModelForm):
    class Meta:
        model = Arquivo_txt
        fields = ["url"]


class TransacoesForms(forms.ModelForm):
    class Meta:
        model = Arquivo_txt
        fields = "__all__"
