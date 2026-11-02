#-*- coding: latin1 -*-
import math

def positivo(num):
    # Verifica se é maior que zero e se é um número inteiro
    if num > 0 and num.is_integer():
        return True
    else:
        print("Digite um valor inteiro e positivo.")
        return False

def calcular_e_mostrar_triangulo(ladoA, ladoB, ladoC):
    # Verifica se forma triângulo e Calcula a área
    if (ladoA + ladoB > ladoC) and (ladoB + ladoC > ladoA) and (ladoC + ladoA > ladoB):
        print("Os valores formam um triângulo!")

        s = (ladoA + ladoB + ladoC) / 2
        area = math.sqrt(s * (s - ladoA) * (s - ladoB) * (s - ladoC))

        print(f"Área do triângulo: {area:.2f}")
        return True
    else:
        print("Os valores não formam um triângulo.")
        return False

ladoA = float(input("Digite um valor A: "))
ladoB = float(input("Digite um valor B: "))
ladoC = float(input("Digite um valor C: "))

positivo(ladoA)
positivo(ladoB)
positivo(ladoC)
calcular_e_mostrar_triangulo(ladoA, ladoB, ladoC)



