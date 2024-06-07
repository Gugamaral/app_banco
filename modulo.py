from datetime import date

def exibir_menu():
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outrubro', 'Novembro', 'Dezembro')
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year

    print(f'\n{dia} de {meses[mes - 1]} de {ano}.\n')

print(f'{'-'*30} APP CADASTRO SENAIBANK {'-'* 30} \n ')

pessoa = {

    'Nome': input('Informe seu nome: '),
    'CPF': input('Informe seu CPF: '),
    'RGg': input('Informe seu RG: '),
    'Data de Nascimento': input('Informe sua data de nascimento: '),
    'Gênero': input('Informe seu gênero: '),
    'e-mail': input('Informe seu e-mail: '),
    'Telefone': input('Informe seu telefone: '),
    'Profissão': input('Informe sua profissão: '),
    
}

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')
    break

