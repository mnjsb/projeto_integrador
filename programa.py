# Software conversor de temperaturas entre Celsius, Fahrenheit, Kelvin e Réamur
# Fontes da pequisa: https://pt.wikipedia.org/wiki/R%C3%A9aumur
#					 http://bit.ly/2PA3sk9
# Repositório do projeto: https://github.com/mnjsb/projeto_integrador

# Autor: Manoel Santiago
# Data: Abril 2019

# Importa a função sleep da biblioteca time
from time import sleep

# importa a biblioteca sys para fechar o programa
import sys

# Importa a biblioteca conversor
import conversor

# Menu de opções
def menu():
    print("")
escolha = -1
while True: # Mostra o menu de opções até que o usuário digite [0] para finalizar o programa
    print("============================================")
    print("       CONVERSOR DE TEMPERATURAS v.1.0      ") # printa o nome do programa
    print("============================================")
    print("\nMenu de opções \n")
    print('''        [1 ] Celsius -> Fahrenheit
        [2 ] Celsius -> Kelvin
        [3 ] Celsius -> Réamur
        [4 ] Fahrenheit -> Celsius
        [5 ] Fahrenheit -> Kelvin
        [6 ] Fahrenheit -> Réamur
        [7 ] Kelvin -> Celsius
        [8 ] Kelvin -> Fahrenheit
        [9 ] Kelvin -> Réamur
        [10] Réamur -> Celsius
        [11] Réamur -> Fahrenheit
        [12] Réamur -> Kelvin
        [0 ] sair''')
    print("")
    print("=============================================")
    print("")

    # Variável que recebe o número da opção escolhida pelo usuário
    escolha = input("Digite uma opção entre [1] a [12] ou [0] para sair >>> ")
  
    if escolha == '1': # Condicional que recebe a opção [1] escolhida pelo usuário na variável "escolha"
        print("Você escolheu opção [1] converter Celsius -> Fahrenheit")
        conversor.c_f() # Chama a função "c_f" da biblioteca  "conversor" (calcula conversão de Celsius -> Fahrenheit) 

    elif escolha == '2': # Condicional que recebe a opção [2] escolhida pelo usuário na variável "escolha"
        print("Você escolheu opção [2] converter Celsius -> Kelvin")
        conversor.c_k() # Chama a função "c_k" da biblioteca  "conversor" (calcula conversão de Celsius -> Kelvin) 
  
    elif escolha == '3': # Condicional que recebe a opção [3] escolhida pelo usuário na variável "escolha"
        print("Você escolheu opção [3] converter Celsius -> Réamur")
        conversor.c_r() # Chama a função "c_r" da biblioteca  "conversor" (calcula conversão de Celsius -> Réamur)
    
    elif escolha == '4': # Condicional que recebe a opção [4] escolhida pelo usuário na variável "escolha"
        print("Você escolheu opção [4] converter Fahrenheit -> Celsius")
        conversor.f_c() # Chama a função "f_c" da biblioteca  "conversor" (calcula conversão de Fahrenheit -> Celsius)
    
    elif escolha == '5': # Condicional que recebe a opção [5] escolhida pelo usuário na variável "escolha"
        print("Você escolheu opção [5] converter Fahrenheit -> Kelvin")
        conversor.f_k() # Chama a função "f_k" da biblioteca  "conversor" (calcula conversão de Fahrenheit -> Kelvin)
    
    elif escolha == '6': # Condicional que recebe a opção [6] escolhida pelo usuário na variável "escolha"
        print("Você escolheu opção [6] converter Fahrenheit -> Réamur")
        conversor.f_r() # Chama a função "f_r" da biblioteca  "conversor" (calcula conversão de Fahrenheit -> Réamur)
    
    elif escolha == '7': # Condicional que recebe a opção [7] escolhida pelo usuário na variável "escolha"
        print("Você escolheu opção [7] converter Kelvin -> Celsius")
        conversor.k_c() # Chama a função "k_c" da biblioteca  "conversor" (calcula conversão de Kelvin -> Celsius)
    
    elif escolha == '8': # Condicional que recebe a opção [8] escolhida pelo usuário na variável "escolha"
        print("Você escolheu opção [8] converter Kelvin -> Fahrenheit")
        conversor.k_f() # Chama a função "k_f" da biblioteca  "conversor" (calcula conversão de Kelvin -> Fahrenheit)
    
    elif escolha == '9': # Condicional que recebe a opção [9] escolhida pelo usuário na variável "escolha"
        print("Você escolheu opção [9] converter Kelvin -> Réamur")
        conversor.k_r() # Chama a função "k_r" da biblioteca  "conversor" (calcula conversão de Kelvin -> Réamur)
    
    elif escolha == '10': # Condicional que recebe a opção [10] escolhida pelo usuário na variável "escolha"
        print("Você escolheu opção [10] converter Réamur -> Celsius")
        conversor.r_c() # Chama a função "r_c" da biblioteca  "conversor" (calcula conversão de Réamur -> Celsius)
    
    elif escolha == '11': # Condicional que recebe a opção [11] escolhida pelo usuário na variável "escolha"
        print("Você escolheu opção [11] converter Réamur -> Fahrenheit")
        conversor.r_f() # Chama a função "r_f" da biblioteca  "conversor" (calcula conversão de Réamur -> Fahrenheit)
    
    elif escolha == '12': # Condicional que recebe a opção [12] escolhida pelo usuário na variável "escolha"
        print("Você escolheu opção [12] converter Réamur -> Kelvin")
        conversor.r_k() # Chama a função "r_k" da biblioteca  "conversor" (calcula conversão de Réamur -> Kelvin)
    
    elif escolha == '0': # Condicional que recebe a opção [0] escolhida pelo usuário na variável "escolha"
        print("Finalizando.........")
        sleep(2) # retarda em 2 segundos
        print("Até a próxima!")
        sleep(2) # retarda em 2 segundos
        sys.exit() # Sair do programa
        
    elif escolha != '': # Condicional que retorna uma mensagem ao usuário caso digite uma opção
                        # ou outro caracter que não consta no menu de opções
        print("Opção Inválida! Digite [0] para finalizar ou tente novamente!")
 
