from django.shortcuts import render
from .models import Transacao_CNAB
from .forms import ArquivosForms, TransacoesForms


def parser_txt(txt):
    ...


def inserir_parse_txt(txt):
    ...


def cadastrar_transacoes(request):
    """
    REGRAS DE CADASTRO
    ESSE CADASTRO APENAS INSERE NA TABELA TRANSACAO O ARQUIVO ESCOLHIDO
    APO ENVIO DO ARQUIVO INSERIDO ELE SOFRERAR UM PARSE COM AS SEGUINTES REGRAS:
    Descrição do campo	Inicio	Fim	Tamanho	Comentário
    Tipo	1	1	1	Tipo da transação
    Data	2	9	8	Data da ocorrência
    Valor	10	19	10	Valor da movimentação. Obs. O valor encontrado no arquivo precisa ser divido por cem(valor / 100.00) para normalizá-lo.
    CPF	20	30	11	CPF do beneficiário
    Cartão	31	42	12	Cartão utilizado na transação
    Hora	43	48	6	Hora da ocorrência atendendo ao fuso de UTC-3
    Dono da loja	49	62	14	Nome do representante da loja
    Nome loja	63	81	19	Nome da loja

    Documentação sobre os tipos das transações
    Tipo	Descrição	Natureza	Sinal
    1	Débito	Entrada	+
    2	Boleto	Saída	-
    3	Financiamento	Saída	-
    4	Crédito	Entrada	+
    5	Recebimento Empréstimo	Entrada	+
    6	Vendas	Entrada	+
    7	Recebimento TED	Entrada	+
    8	Recebimento DOC	Entrada	+
    9	Aluguel	Saída	-
    """
    ...


def index(request):
    data = {"form": ArquivosForms()}
    data["table"] = Transacao_CNAB.objects.all()
    return render(request, "index.html", data)


def alterar_transacao(request):
    """
    REGRAS PARA ALTERAR TRANSACAO
    NENHUMA
    """
