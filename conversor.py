# Biblioteca que irá realizar os cálculos entre Celsius, Fahrenheit, Kelvin e Réamur
# Fonte da pequisa dos cálculos: https://pt.wikipedia.org/wiki/R%C3%A9aumur
#                                http://bit.ly/2PA3sk9
# Repositório do projeto: https://github.com/mnjsb/projeto_integrador

# Autor: Manoel Santiago
# Data: Abril 2019

''' Função que realiza o cálculo de conversão de temperatura de ºCelsius para ºFahrenheit
e mostra o resultado para o usuário '''
def c_f():					
	try: # Início do tratamento de excessão
		c = float(input("Informe a temperatura em ºCelsius: ")) 
		f = ((9 * c) / 5) + 32
		print("A temperatura de {}º Celsius corresponde à {:.2f}º Fahrenheit!".format(c, f))
	except Exception: # Excessão caso usuário digite valores que não sejam números reais
		print("Valor inválido. Digite somente números reais sem ',', exemplo 22.76")    
		return c_f() # Retorna à função após o aviso acima

''' Função que realiza o cálculo de conversão de temperatura de ºCelsius para ºKelvin
e mostra o resultado para o usuário '''
def c_k():
	try: # Início do tratamento de excessão
	    c = float(input("Informe a temperatura em ºCelsius: "))
	    k = c + 273.15
	    print("A temperatura de {}º Celsius corresponde à {:.2f}º Kelvin!".format(c, k))
	except Exception: # Excessão caso usuário digite valores que não sejam números reais
		print("Valor inválido. Digite somente números reais sem ',', exemplo 22.76")    
		return c_k() # Retorna à função após o aviso acima

''' Função que realiza o cálculo de conversão de temperatura de ºCelsius para ºReamur
e mostra o resultado para o usuário '''
def c_r():
	try: # Início do tratamento de excessão
	    c = float(input("Informe a temperatura em ºCelsius: "))
	    r = c * 4/5
	    print("A temperatura de {}º Celsius corresponde à {:.2f}º Réamur!".format(c, r))
	except Exception: # Excessão caso usuário digite valores que não sejam números reais
		print("Valor inválido. Digite somente números reais sem ',', exemplo 22.76")    
		return c_r() # Retorna à função após o aviso acima	 

''' Função que realiza o cálculo de conversão de temperatura de ºFahrenheit para ºCelsius
e mostra o resultado para o usuário '''
def f_c():
	try: # Início do tratamento de excessão
	    f = float(input("Informe a temperatura em ºFahrenheit: "))
	    c = (f - 32) * 5/9
	    print("A temperatura de {}º Fahrenheit corresponde à {:.2f}º Celsius!".format(f, c))
	except Exception: # Excessão caso usuário digite valores que não sejam números reais
		print("Valor inválido. Digite somente números reais sem ',', exemplo 22.76")    
		return f_c() # Retorna à função após o aviso acima

''' Função que realiza o cálculo de conversão de temperatura de ºFahrenheit para ºKelvin
e mostra o resultado para o usuário '''
def f_k():
	try: # Início do tratamento de excessão
	    f = float(input("Informe a temperatura em ºFahrenheit: "))
	    k = (f - 32) * 5/9 + 273.15
	    print("A temperatura de {}º Fahrenheit corresponde à {:.2f}º Kelvin!".format(f, k))
	except Exception: # Excessão caso usuário digite valores que não sejam números reais
		print("Valor inválido. Digite somente números reais sem ',', exemplo 22.76")    
		return f_k() # Retorna à função após o aviso acima

''' Função que realiza o cálculo de conversão de temperatura de ºFahrenheit para ºReamur
e mostra o resultado para o usuário '''
def f_r():
	try: # Início do tratamento de excessão
		f = float(input("Informe a temperatura em ºFahrenheit: "))
		r = (f - 32) * 4/9
		print("A temperatura de {}º Fahrenheit corresponde à {:.2f}º Réamur!".format(f, r))
	except Exception: # Excessão caso usuário digite valores que não sejam números reais
		print("Valor inválido. Digite somente números reais sem ',', exemplo 22.76")    
		return f_r() # Retorna à função após o aviso acima	

''' Função que realiza o cálculo de conversão de temperatura de ºKelvin para ºCelsius
e mostra o resultado para o usuário '''
def k_c():
	try: # Início do tratamento de excessão
	    k = float(input("Informe a temperatura em ºKelvin: "))
	    c = k - 273.15
	    print("A temperatura de {}º Kelvin corresponde à {:.2f}º Celsius!".format(k, c))
	except Exception: # Excessão caso usuário digite valores que não sejam números reais
		print("Valor inválido. Digite somente números reais sem ',', exemplo 22.76")    
		return k_c() # Retorna à função após o aviso acima

''' Função que realiza o cálculo de conversão de temperatura de ºKelvin para ºFahrenheit
e mostra o resultado para o usuário '''
def k_f():
	try: # Início do tratamento de excessão
	    k = float(input("Informe a temperatura em ºKelvin: "))
	    f = (k - 273.15) * 9/5 + 32
	    print("A temperatura de {}º Kelvin corresponde à {:.2f}º Fahrenheit!".format(k, f))
	except Exception: # Excessão caso usuário digite valores que não sejam números reais
		print("Valor inválido. Digite somente números reais sem ',', exemplo 22.76")    
		return k_f() # Retorna à função após o aviso acima

''' Função que realiza o cálculo de conversão de temperatura de ºKelvin para ºReamur
e mostra o resultado para o usuário '''
def k_r():
	try: # Início do tratamento de excessão
	    k = float(input("Informe a temperatura em ºKelvin: "))
	    r = (k - 273.15) * 0.8
	    print("A temperatura de {}º Kelvin corresponde à {:.2f}º Réamur!".format(k, r))
	except Exception: # Excessão caso usuário digite valores que não sejam números reais
		print("Valor inválido. Digite somente números reais sem ',', exemplo 22.76")    
		return k_r() # Retorna à função após o aviso acima

''' Função que realiza o cálculo de conversão de temperatura de ºReamur para ºCelsius
e mostra o resultado para o usuário '''
def r_c():
	try: # Início do tratamento de excessão
	    r = float(input("Informe a temperatura em ºRéamur: "))
	    c = r * 5/4
	    print("A temperatura de {}º Réamur corresponde à {:.2f}º Celsius!".format(r, c))
	except Exception: # Excessão caso usuário digite valores que não sejam números reais
		print("Valor inválido. Digite somente números reais sem ',', exemplo 22.76")    
		return r_c() # Retorna à função após o aviso acima

''' Função que realiza o cálculo de conversão de temperatura de ºReamur para ºFahrenheit
e mostra o resultado para o usuário '''
def r_f():
	try: # Início do tratamento de excessão
	    r = float(input("Informe a temperatura em ºRéamur: "))
	    f = r * 9/4 + 32
	    print("A temperatura de {}º Réamur corresponde à {:.2f}º Fahrenheit!".format(r, f))
	except Exception: # Excessão caso usuário digite valores que não sejam números reais
		print("Valor inválido. Digite somente números reais sem ',', exemplo 22.76")    
		return r_f() # Retorna à função após o aviso acima

''' Função que realiza o cálculo de conversão de temperatura de °Reamur para ºKelvin
e mostra o resultado para o usuário '''
def r_k():
	try: # Início do tratamento de excessão
	    r = float(input("Informe a temperatura em ºRéamur: "))
	    k = r * 5/4 + 273.15
	    print("A temperatura de {}º Réamur corresponde à {:.2f}º Kelvin!".format(r, k))
	except Exception: # Excessão caso usuário digite valores que não sejam números reais
		print("Valor inválido. Digite somente números reais sem ',', exemplo 22.76")    
		return r_k() # Retorna à função após o aviso acima