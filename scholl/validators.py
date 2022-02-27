from validate_docbr import CPF
from datetime import datetime

# Validating Students
def valid_name(name):
    name = name.replace(" ", "")
    return name.isalpha()

def valid_rg(rg):
    return len(rg) == 9

def valid_cpf_characters(cpf):
    return len(cpf) == 11
 
def valid_cpf(cpf):
    validator = CPF()
    return validator.validate(cpf)

def valid_date(date_birth):
    today_date = datetime.now()
    current_year = today_date.strftime("%Y")
    print(int(date_birth.strftime('%Y')) < int(current_year))
    return int(date_birth.strftime('%Y')) < int(current_year)

# Validating Courses
def valid_code(cod):
    return len(cod) == 5