#logorithm calculator
#imports
import math
import os

#clear cli
os.system('cls')

#menü
def menu():
    input_menu = int(input(" 1 LOG | 2 LOG + LOG | 3 LOG - LOG | 4 LOG x LOG | 5 LOG / LOG | 6 Infos | 7 Exit\n"))
    return input_menu

#log funktion
def log_math():
    basis = int(input("Basis: "))#standart 10
    exponent = int(input("Exponent: "))
    print(math.log(exponent, basis))

#log addition funktion
def log_plus_log():
    basis = int(input("Basis: "))#standart 10
    exponent = int(input("Exponent "))
    log1 = math.log(exponent, basis)
    basis2 = int(input("Basis: "))#standart 10
    exponent2 = int(input("Exponent: "))
    log2 = math.log(exponent2, basis2)
    print(log1 + log2)


#log subtraktion funktion
def log_minus_log():
    basis = int(input("Basis: "))#standart 10
    exponent = int(input("Exponent: "))
    log1 = math.log(exponent, basis)
    basis2 = int(input("Basis: "))#standart 10
    exponent2 = int(input("Exponent: "))
    log2 = math.log(exponent2, basis2)
    print(log1 - log2)

#log multiplikation funktion
def log_m_log():
    basis = int(input("Basis: "))#standart 10
    exponent = int(input("Exponent: "))
    log1 = math.log(exponent, basis)
    basis2 = int(input("Basis: "))#standart 10
    exponent2 = int(input("Exponent: "))
    log2 = math.log(exponent2, basis2)
    print(log1 * log2)

#log division funktion
def log_d_log():
    basis = int(input("Basis: "))#standart 10
    exponent = int(input("Exponent: "))
    log1 = math.log(exponent, basis)
    basis2 = int(input("Basis: "))#standart 10
    exponent2 = int(input("Exponent: "))
    log2 = math.log(exponent2, basis2)
    return(log1 / log2)

def information():
    print("This is a small Programming Project by Giorgio Jacomella for the calculation of logorythms \nGithub: https://github.com/GiorgioJacomella \n \n")


#main part
i = True
while i == True:
    input_menu = menu()
    if input_menu == 1:
        log_math()
    elif input_menu == 2:
        log_plus_log()
    elif input_menu == 3:
        log_minus_log()
    elif input_menu == 4:
        log_m_log()
    elif input_menu == 5:
        log_d_log()
    elif input_menu == 6:
        information()
    elif input_menu == 7:
        i = False
    else:
        print("There has been an Error")