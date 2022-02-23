from validate_docbr import CPF
import datetime

# Validando Alunos
def nome_valido(nome):
    nome = nome.replace(" ", "")
    return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9

def cpf_caracteres_valido(cpf):
    return len(cpf) == 11
 
def cpf_valido(cpf):
    validator = CPF()
    return validator.validate(cpf)

def data_valida(data_nascimento):
    data_hoje = datetime.date.today()
    ano_atual = data_hoje.strftime("%Y")
    return int(data_nascimento.strftime('%Y')) < int(ano_atual)

# Validando Curso
def codigo_valido(codigo):
    return len(codigo) == 5