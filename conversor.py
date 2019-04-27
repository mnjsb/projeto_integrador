# Biblioteca que irá realizar os cálculos entre Celsius, Fahrenheit, Kelvin e Réamur
# Fonte da pequisa dos cálculos: https://pt.wikipedia.org/wiki/R%C3%A9aumur
#                                http://bit.ly/2PA3sk9

# Autor: Manoel Santiago
# Data: Abril 2019

''' Função que realiza o cálculo de conversão de temperatura de ºCelsius para ºFahrenheit
e mostra o resultado para o usuário '''
def c_f():   
    c = float(input("Informe a temperatura em ºCelsius: "))
    f = ((9 * c) / 5) + 32
    print("A temperatura de {} ºCelsius corresponde à {:.2f} ºFahrenheit!".format(c, f))
		
''' Função que realiza o cálculo de conversão de temperatura de ºCelsius para ºKelvin
e mostra o resultado para o usuário '''
def c_k():
    c = float(input("Informe a temperatura em ºCelsius: "))
    k = c + 273.15
    print("A temperatura de {} ºCelsius corresponde à {:.2f} ºKelvin!".format(c, k))
	
''' Função que realiza o cálculo de conversão de temperatura de ºCelsius para ºReamur
e mostra o resultado para o usuário '''
def c_r():
    c = float(input("Informe a temperatura em ºCelsius: "))
    r = c * 4/5
    print("A temperatura de {} ºCelsius corresponde à {:.2f} ºRéamur!".format(c, r))
		
''' Função que realiza o cálculo de conversão de temperatura de ºFahrenheit para ºCelsius
e mostra o resultado para o usuário '''
def f_c():
    f = float(input("Informe a temperatura em ºFahrenheit: "))
    c = (f - 32) * 5/9
    print("A temperatura de {} ºFahrenheit corresponde à {:.2f} ºCelsius!".format(f, c))
	
''' Função que realiza o cálculo de conversão de temperatura de ºFahrenheit para ºKelvin
e mostra o resultado para o usuário '''
def f_k():
    f = float(input("Informe a temperatura em ºFahrenheit: "))
    k = (f - 32) * 5/9 + 273.15
    print("A temperatura de {} ºFahrenheit corresponde à {:.2f} ºKelvin!".format(f, k))
	
''' Função que realiza o cálculo de conversão de temperatura de ºFahrenheit para ºReamur
e mostra o resultado para o usuário '''
def f_r():
    f = float(input("Informe a temperatura em ºFahrenheit: "))
    r = (f - 32) * 4/9
    print("A temperatura de {} ºFahrenheit corresponde à {:.2f} ºRéamur!".format(f, r))
	
''' Função que realiza o cálculo de conversão de temperatura de ºKelvin para ºCelsius
e mostra o resultado para o usuário '''
def k_c():
    k = float(input("Informe a temperatura em ºKelvin: "))
    c = k - 273.15
    print("A temperatura de {} ºKelvin corresponde à {:.2f} ºCelsius!".format(k, c))
		
''' Função que realiza o cálculo de conversão de temperatura de ºKelvin para ºFahrenheit
e mostra o resultado para o usuário '''
def k_f():
    k = float(input("Informe a temperatura em ºKelvin: "))
    f = (k - 273.15) * 9/5 + 32
    print("A temperatura de {} ºKelvin corresponde à {:.2f} ºFahrenheit!".format(k, f))
	
''' Função que realiza o cálculo de conversão de temperatura de ºKelvin para ºReamur
e mostra o resultado para o usuário '''
def k_r():
    k = float(input("Informe a temperatura em ºKelvin: "))
    r = (k - 273.15) * 0.8
    print("A temperatura de {} ºKelvin corresponde à {:.2f} ºRéamur!".format(k, r))
	
''' Função que realiza o cálculo de conversão de temperatura de ºReamur para ºCelsius
e mostra o resultado para o usuário '''
def r_c():
    r = float(input("Informe a temperatura em ºRéamur: "))
    c = r * 5/4
    print("A temperatura de {} ºRéamur corresponde à {:.2f} ºCelsius!".format(r, c))
	
''' Função que realiza o cálculo de conversão de temperatura de ºReamur para ºFahrenheit
e mostra o resultado para o usuário '''
def r_f():
    r = float(input("Informe a temperatura em ºRéamur: "))
    f = r * 9/4 + 32
    print("A temperatura de {} ºRéamur corresponde à {:.2f} ºFahrenheit!".format(r, f))
		
''' Função que realiza o cálculo de conversão de temperatura de °Reamur para ºKelvin
e mostra o resultado para o usuário '''
def r_k():
    r = float(input("Informe a temperatura em ºRéamur: "))
    k = r * 5/4 + 273.15
    print("A temperatura de {} ºRéamur corresponde à {:.2f} ºKelvin!".format(r, k))