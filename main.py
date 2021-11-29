# # Prompt the user to enter a word
# # and assign it to the user_word variable.
# user_word = input("Informe uma palavra: ").upper()

# # for letter in user_word:
# #     if letter != "A" and letter != "E" and letter != "I" and letter != "O" and letter != "U":
# #         print(letter)

# for letter in user_word:
#     if letter == "A": continue
#     if letter == "E": continue
#     if letter == "I": continue
#     if letter == "O": continue
#     if letter == "U": continue
#     print(letter)

# ====================================================================


# word_without_vowels = ""
# user_word = input("Informe uma palavra: ").upper()

# for letter in user_word:
#     if letter == "A": continue
#     if letter == "E": continue
#     if letter == "I": continue
#     if letter == "O": continue
#     if letter == "U": continue
#     word_without_vowels += letter
    
# print(word_without_vowels)

# =====================================================================

# blocks = int(input("Enter the number of blocks: "))
# total_blocos = 0
# height = 0
# #
# # Write your code here.
# #	

# while True:
#     if total_blocos > blocks:
#         height -= 1
#         break
#     else:
#         height += 1
#         total_blocos += height

# print("The height of the pyramid:", height)

# ======================================================================

# par c0 / 2
# impar 3 * c0 + 1
# se != 1 ir para o par

# c0 = int(input("Informe um número: "))
# steps = 0
# while True:
#     if c0 == 1:
#         break
#     elif c0 % 2 == 0:
#         c0 = int(c0 / 2)
#         steps += 1
#     elif c0 % 2 == 1:
#         c0 = 3 * c0 + 1
#         steps += 1
#     print(c0)

# print("Steps =", steps)


# ========================================================================
# n = 0

# while n != 3:
#     print(n)
#     n += 1
# else:
#     print(n, "else")

# print()

# for i in range(0, 3):
#     print(i)
# else:
#     print(i, "else")

# ==============================================

# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         # Line of code.
#         break
#     # Line of code.
#     print(ch, end="")
# print()
# ===============================================================

# for digit in "0165031806510":
#     if digit == "0":
#         # Line of code.
#         print("x", end="")
#         # Line of code.
#         continue
#     # Line of code.
#     print(digit, end="")
    
# ======================================================================
# for i in range(0, 6, 3):
#     print(i)

# =============================================
# b = bytes([0x41, 0x42, 0x43, 0x44])
# print(b)

# s = "Str"
# print(s)

# # print(s + b)
# print(s + b.decode('utf-8'))

# print(s.encode('utf-32') + b)
# ======================================================
# from string import Template

# def main():
#     # Formatação tradicional usando o método format()
#     frase = "Você está assistindo {0} com {1}".format(
#         "Python Avançado", "Jessica Temporal")
#     print(frase)

#     # TODO: Crie um template com placeholders
#     templ = Template("Você está assistindo ${curso} com ${instrutora}")

#     # TODO: Use o método substitute passando argumentos nomeados
#     frase_2 = templ.substitute(
#         curso="Python Avançado",
#         instrutora="Jessica Temporal"
#     )
#     print(frase_2)

#     # TODO: Use o método substitute com um dicionário
#     dados = {
#         "curso": "Python Avançado",
#         "instrutora": "Jessica Temporal"
#     }
#     frase_3 = templ.substitute(dados)
#     print(frase_3)

# main()

# ================================================

# my_list = [1, 2, 5, 4]
# swapped = True
# num = int(input("How many elements do you want to sort: "))

# for i in range(num):
#     val = float(input("Enter a list element: "))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list)):
#         print(i)
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nSorted:")
# print(my_list)

# ==================================

# a = 3
# b = 1
# c = 2

# lst = [a, c, b]
# lst.sort()

# print(lst)

# =====================================================

# Temperatura média mensal ao meio dia 

# temps = [[0.0 for h in range(24)] for d in range(31)]
# #
# # The matrix is magically updated here.
# #

# total = 0.0

# for day in temps:
#     total += day[11]

# average = total / 31

# print("Average temperature at noon:", average)


# ==============================================================

# Encontrando a temperatura mais alta durante todo o mês - veja o código:

# temps = [[0.0 for h in range(24)] for d in range(31)]
# #
# # The matrix is magically updated here.
# #

# highest = -100.0

# for day in temps:
#     for temp in day:
#         if temp > highest:
#             highest = temp

# print("The highest temperature was:", highest)

# ===============================================================

# Contando os dias em que a temperatura ao meio-dia era de pelo menos 20 ℃:

# temps = [[0.0 for h in range(24)] for d in range(31)]
# #
# # The matrix is magically updated here.
# #

# hot_days = 0

# for day in temps:
#     if day[11] > 20.0:
#         hot_days += 1

# print(hot_days, "days were hot.")

# ==================================================================

# Array com 3 edificios, 15 andares, 20 quartos por andar.

# rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# ===========================================================

# Alugando um quarto no edificio 2, andar 10, quarto 14

# rooms[1][9][13] = True

# ================================================================

# Verificando se existe quarto vago no edificio 3, andar 15

# vacancy = 0

# for room_number in range(20):
#     if not rooms[2][14][room_number]:
#         vacancy += 1

# ====================================================================

# a = 1
# b = 0
# c = a & b
# d = a | b
# e = a ^ b
# print(c + d + e)

# ===================================
# for i in range(1):
#     print('a')
# else:
#     print("a")

# =================================
# my_list = [[0, 1, 2, 3] for i in range(2)]
# print(my_list[2][0])

# ========================

# my_list = [1, 2, 3, 4]
# print(my_list[-3:-2])

# ===============================

# n = [1,2,3]
# vals = n
# del vals[1:2]
# print(n)
# print(vals)
# ==============================
# n = [1,2,3]
# v = n[-1:-2]
# print(v)
# print(n)

# ========================
# v = [0,1,2]
# v.insert(0,1)
# del v[1]
# print(v)

# =============================

# l1 = [1,2,3]
# l2 = []
# for v in l1:
#     l2.insert(0, v)
# print(l2)
# ==============================

# l = [1,2,3]
# for v in range(len(l)):
#     l.insert(1, l[v])
# print(l)

# ============================

# t = [[3-i for i in range (3)] for j in range (3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)

# ==================================

# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         continue
#     print("#")


# ===========================================

# Verificar com duas listas se o ano é (True) ou não Bissexto (False)

# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True


# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
# 	yr = test_data[i]
# 	print(yr,"->",end="")
# 	result = is_year_leap(yr)
# 	if result == test_results[i]:
# 		print("OK")
# 	else:
# 		print("Failed")


# =====================================

# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# def days_in_month(year, month):
#     if month == 2:
#         if is_year_leap(year):
#             return 29
#         else:
#             return 28
#     elif month in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
#     elif month in [4, 6, 9, 11]:
#         return 30
        
        
# test_years = [1900, 2000, 2016, 1987, 2021]
# test_months = [2, 2, 12, 11, 12]
# test_results = [28, 29, 31, 30, 31]
# for i in range(len(test_years)):
# 	yr = test_years[i]
# 	mo = test_months[i]
# 	print(yr, mo, "->", end="")
# 	result = days_in_month(yr, mo)
# 	if result == test_results[i]:
# 		print("OK")
# 	else:
# 		print("Failed")

# =============================================

# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# def days_in_month(year, month):
#     if month == 2:
#         if is_year_leap(year):
#             return 29
#         else:
#             return 28
#     elif month in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
#     elif month in [4, 6, 9, 11]:
#         return 30

# def day_of_year(year, month, day):
#     if (month >= 1) and (month <= 12) and (year > 0) and (day >= 1) and (day <= days_in_month(year, month)):
#         final = 0
#         for i in range(1, month):
#             final += days_in_month(year, i)
#         return final + day
#     else:
#         return

# print(day_of_year(2021, 12, 31))

# ============================================

# def is_prime(num):
#     resto = 0
#     for j in range(2, 900):
#         if num % j == 0:
#             resto += 1
#         if resto > 1:
#             return False
#             break
#     if resto == 1:
#         return True

# for i in range(1, 100):
# 	if is_prime(i + 1):
# 			print(i + 1, end=" ")
# print()

# =================================================
# O consumo de combustível de um carro pode ser expresso de várias maneiras. Por exemplo, na Europa, é mostrado como a quantidade de combustível consumido por 100 quilómetros.
# Nos EUA, é mostrado como o número de milhas percorridas por um carro utilizando um galão de combustível.
# A sua tarefa é escrever um par de funções convertendo l/100 km em mpg, e vice-versa.

# As funções:

# são nomeadas liters_100km_to_miles_gallon e miles_gallon_to_liters_100km respetivamente;
# tome um argumento (o valor correspondente aos seus nomes)
# Complete o código no editor.

# Execute o seu código e verifique se o seu output é o mesmo que o nosso.

# Aqui estão algumas informações para o ajudar:

# 1 milha americana = 1609,344 metros;
# 1 galão americano = 3,785411784 litros.

# Output esperado
# 60.31143162393162
# 31.36194444444444
# 23.52145833333333
# 3.9007393587617467
# 7.490910297239916
# 10.009131205673757
# ---

# def liters_100km_to_miles_gallon(liters):
    

# def miles_gallon_to_liters_100km(miles):
# #
# # Write your code here
# #

# print(liters_100km_to_miles_gallon(3.9))
# print(liters_100km_to_miles_gallon(7.5))
# print(liters_100km_to_miles_gallon(10.))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))

# ==========================================================

# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1

#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum


# for n in range(1, 10):  # testing
#     print(n, "->", fib(n))

# ========================================================

# def teste(n):
#     n += 2
#     if n < 20:
#         print("dentro1")
#         teste(n+1)
#         print("Dentro2", n)
#     return n

# # print()
# print("fora", teste(1))
# # print(retorno)

# ======================================================

# def fun(a):
#     if a > 30:
#         print("1")
#         return 3
#     else:
#         print("2")
#         return a + fun(a + 3)


# print(fun(25))

# ================================================================

# tuple_1 = (1, 2, 4, 8)
# tuple_2 = 1., .5, .25, .125
# one_ele = (1,)
# empyt_tuple = ()
# print(tuple_1)
# print(tuple_2)
# print(type(tuple_1))
# print(type(one_ele))

# =============================================

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
# empty_dictionary = {}

# print(dictionary)
# print(phone_numbers)
# print(empty_dictionary)

# ====================================================================

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# words = ['cat', 'lion', 'horse']

# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, "is not in dictionary")

# =========================================================================

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# for key in sorted(dictionary.keys()):
#     print(key, "->", dictionary[key])

# ================================================================================

# school_class = {}

# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
    
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
# 	    break
    
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
        
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)

# print(school_class)

# =====================================================================

# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }

# for item in pol_eng_dictionary:
#     print(item) 

# # outputs: zamek
# #          woda
# #          gleba

# =============================================================

# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }

# for key, value in pol_eng_dictionary.items():
#     print("Pol/Eng ->", key, ":", value)

# ===============================================================

# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }

# if "zaek" in pol_eng_dictionary:
#     print("Yes")
# else:
#     print("No")

# ===================================================================
# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}

# for item in (d1, d2):
#     d3.update(item)

# print(d3)

# ====================================================================

# colors = (("green", "#008000"), ("blue", "#0000FF"))

# colors_dictionary = dict(colors)
# print(colors_dictionary)
# =================================================================

# my_dictionary = {"A": 1, "B": 2}
# copy_my_dictionary = my_dictionary.copy()
# my_dictionary.clear()

# print(copy_my_dictionary)

# =========================================================================

#     - Cenário
# A sua tarefa é escrever um programa simples que finja jogar tic-tac-toe com o utilizador. Para lhe facilitar as coisas, decidimos simplificar o jogo. Aqui estão os nossos pressupostos:

#     * o computador (ou seja, o seu programa) deve jogar o jogo utilizando 'X's;
#     * o utilizador (por exemplo, você) deve jogar o jogo utilizando 'O's;
#     * o primeiro movimento pertence ao computador - coloca sempre o seu primeiro 'X' no meio do tabuleiro;
#     * todos os quadrados são numerados fila a fila começando por 1 (veja a sessão de exemplo abaixo, para referência)
#     * o utilizador introduz a sua jogada inserindo o número do quadrado que escolhe - o número deve ser válido, ou seja, deve ser um número inteiro, deve ser maior do que 0 e menos do que 10, e não pode apontar para um campo que já esteja ocupado;
#     * o programa verifica se o jogo terminou - há quatro vereditos possíveis: o jogo deve continuar, ou o jogo termina com um empate, a sua vitória ou a vitória do computador;
#     * o computador responde com a sua jogada e a verificação é repetida;
#     * não implemente nenhuma forma de inteligência artificial - uma escolha de campo aleatória feita pelo computador é suficientemente boa para o jogo.

# A sessão de exemplo com o programa pode ter a aparência seguinte:

#     - Requisitos
# Implemente as seguintes características:

#     * o tabuleiro deve ser armazenado como uma lista de três elementos, enquanto cada elemento é outra lista de três elementos (as listas internas representam linhas) de modo a que todos os quadrados possam ser acedidos utilizando a seguinte sintaxe:

#         board[row][column]


#     * cada um dos elementos da lista interna pode conter 'O', 'X', ou um dígito que representa o número do quadrado (tal quadrado é considerado livre)
#     * a aparência do tabuleiro deve ser exatamente a mesma que a apresentada no exemplo.
#     * implemente as funções definidas para si no editor.

# O desenho de um número inteiro aleatório pode ser feito utilizando uma função Python chamada randrange(). O programa de exemplo abaixo mostra como utilizá-lo (o programa imprime dez números aleatórios de 0 a 8).

# Nota: a instrução from-import fornece um acesso à função randrange definida dentro de um módulo externo de Python chamado random.

#         from random import randrange

#         for i in range(10):
#             print(randrange(8))


# def display_board(board):
#     # The function accepts one parameter containing the board's current status
#     # and prints it out to the console.


# def enter_move(board):
#     # The function accepts the board current status, asks the user about their move, 
#     # checks the input and updates the board according to the user's decision.


# def make_list_of_free_fields(board):
#     # The function browses the board and builds a list of all the free squares; 
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.


# def victory_for(board, sign):
#     # The function analyzes the board status in order to check if 
#     # the player using 'O's or 'X's has won the game


# def draw_move(board):
#     # The function draws the computer's move and updates the board.


# ========================================================================
# from platform import python_implementation, python_version_tuple

# print(python_implementation())
# for atr in python_version_tuple():
#     print(atr)

# ============================================================

# def mysplit(strng):
#     #
#     # put your code here
#     #
#     if strng.isspace() or strng == "":
#         lista = []
#         return lista
#     for ch in strng:
        
#         if ch != " ":
#             print(ch)
#             # lista.append(ch)
#             # temp += ch
#             # if ch == " ":
#             #     lista = []
#             #     lista.append(temp)
#             #     return lista
        
    


# # print(mysplit("To be or not to be, that is the question"))
# # print(mysplit("To be or not to be,that is the question"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))



# ====================================================================================

# # Caesar cipher.
# text = input("Enter your message: ")
# cipher = ''
# for char in text:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) + 1
#     if code > ord('Z'):
#         code = ord('A')
#     cipher += chr(code)

# print(cipher)


# ===========================================================================

# # Caesar cipher - decrypting a message.
# cipher = input('Enter your cryptogram: ')
# text = ''
# for char in cipher:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) - 1
#     if code < ord('A'):
#         code = ord('Z')
#     text += chr(code)

# print(text)

# ===============================================================================

# # Numbers Processor.

# line = input("Enter a line of numbers - separate them with spaces: ")
# strings = line.split()
# total = 0
# try:
#     for substr in strings:
#         total += float(substr)
#     print("The total is:", total)
# except:
#     print(substr, "is not a number.")

# ====================================================================================

# # IBAN Validator.
# iban = input("Enter IBAN, please: ")
# iban = iban.replace(' ','')

# if not iban.isalnum():
#     print("You have entered invalid characters.")
# elif len(iban) < 15:
#     print("IBAN entered is too short.")
# elif len(iban) > 31:
#     print("IBAN entered is too long.")
# else:
#     iban = (iban[4:] + iban[0:4]).upper()
#     iban2 = ''
#     for ch in iban:
#         if ch.isdigit():
#             iban2 += ch
#         else:
#             iban2 += str(10 + ord(ch) - ord('A'))
#     iban = int(iban2)
#     if iban % 97 == 1:
#         print("IBAN entered is valid.")
#     else:
#         print("IBAN entered is invalid.")

# ===================================================================================

# # Caesar cipher aprimorado.
# text = input("Enter your message: ")

# while True:
#     interval = int(input("Informe um intervalo de deslocamento entre 1 e 25: "))

#     if interval < 1 or interval > 25:
#         print("Intervalo inválido!")
#     else:
#         break


# cipher = ''
# for char in text:
#     if not char.isalpha():
#         cipher += str(char)
#         continue
#     code = ord(char) + interval
#     if code > ord('Z') and char.isupper():
#         if code > (ord('Z') + 1):#and interval > 1:
#             resto = interval - (ord('Z') - ord(char)) - 1
#             code = ord('A') + resto
#         else:
#             code = ord('A')

#     elif code > ord('z') and char.islower():
#         if code > (ord('z') + 1):
#             resto = interval - (ord('z') - ord(char)) - 1
#             code = ord('a') + resto
#         else:
#             code = ord('a')

#     cipher += chr(code)

# print(cipher)

# ===========================================================================================

# data_nasc = input("Informe sua Data de Nascimento: ")
# soma = 0
# total_final = 0
# for numData in data_nasc:
#     soma += int(numData)

# for numSoma in str(soma):
#     total_final += int(numSoma)

# print(total_final)

# ==============================================================================================







