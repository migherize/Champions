import random

lista = ["rojo", "amarillo", "azul","verde","morado","blanco","negro"]

for i in range(0,8):
	random.shuffle(lista)
	print("primero ", lista.pop(0))