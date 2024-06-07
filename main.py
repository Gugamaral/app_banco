import math
import os
from modulo import *

if __name__ == '__main__':
    while True:
        exibir_menu()
        opcao = input('Insira seu nome completo: ')
        os.system('cls')

        match opcao:
            case '1':
                nomes = opcao
                print(f'Nome {inserir_nome}')
                continue
            
            case _:
                break
         