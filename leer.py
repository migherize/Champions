print("hola leer archivo")
archivo = open('jugadores.txt')
n = 32
m = 3
matriz = []

jugadores = []

#lleno matriz vacia
for i in range(n):
	matriz.append([])
	for j in range(m):
		matriz[i].append(None)


#Para leer una linea
linea = archivo.readline()

#Para leer linea por linea
while linea != '':
	for i in range(n):
		jugador = linea[3:]
		jugadores.append(jugador)
		inf_jugador =jugador.split()
		#print(inf_jugador)
		for j in range(m):
			inf = inf_jugador.pop(0)
			matriz[i][j] = inf
			#print(inf)

		linea = archivo.readline()

#for a in jugadores:
	#print(a)

print("primero", matriz[0])

for j in range(n):
	for i in range(n-1):
		if matriz[i][1] < matriz [i+1][1]:
			aux = matriz[i]
			matriz[i] = matriz [i+1]
			matriz[i+1] = aux


for i in range(n):
	print("m ", matriz[i][1], " ",matriz[i][0] )



archivo.close()