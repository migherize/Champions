import sys 
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QButtonGroup
from bandera import banderas
from grupos import Ui_grupos
from resultadoA import Ui_ResultadoA
from resultadoB import Ui_ResultadoB
from resultadoC import Ui_ResultadoC
from resultadoD import Ui_ResultadoD
from resultadoE import Ui_ResultadoE
from resultadoF import Ui_ResultadoF
from resultadoG import Ui_ResultadoG
from resultadoH import Ui_ResultadoH
from sorteos import Ui_sorteos
from octavos import Ui_Octavos
from cuartos import Ui_Cuartos
import os.path as path
import random


n = 32
m = 3
matriz = []
primeros = []
segundos = []
cuartos = []
band = 0
semifinal = []
final = []
campeon = []

#lleno matriz vacia
for i in range(n):
	matriz.append([])
	for j in range(m):
		matriz[i].append(None)

#abrimos archivo de jugadores
archivo = open('jugadores.txt')

#Para leer una linea
linea = archivo.readline()

#Para leer linea por linea
while linea != '':
	for i in range(n):
		jugador = linea[3:]
		inf_jugador =jugador.split()
		for j in range(m):
			inf = inf_jugador.pop(0)
			matriz[i][j] = inf

		linea = archivo.readline()

archivo.close()

#orrdenamiento de mayor a menor
for j in range(n):
	for i in range(n-1):
		if matriz[i][1] < matriz [i+1][1]:
			aux = matriz[i]
			matriz[i] = matriz [i+1]
			matriz[i+1] = aux

qtCreatorFile = "inicio.ui" # Nombre del archivo aquí. 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile) 

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow): 

	def __init__(self): 
		QtWidgets.QMainWindow.__init__(self) 
		Ui_MainWindow.__init__(self) 
		self.setupUi(self)
		self.pushButton.clicked.connect(self.abrir)
		self.pushButton_2.clicked.connect(self.cerrar)

	#Funcion para que el boton me lleve a la otra ventana.
	def abrir (self):

		self.ventana = QtWidgets.QMainWindow()
		self.ui = Ui_grupos()
		self.ui.setupUi(self.ventana)
		self.ventana.show() #Para ver

		#Para Banderas ELO + NickName

		#Grupo A
		b = banderas(matriz[0][2])
		self.ui.label_A1.setStyleSheet(b.mostrar_bandera())
		self.ui.label_1.setText(str('  ' + matriz[0][1]+ '  ' + matriz[0][0]))

		b = banderas(matriz[8][2])
		self.ui.label_A2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_2.setText(str('  ' + matriz[8][1]+ '  ' + matriz[8][0]))

		b = banderas(matriz[16][2])
		self.ui.label_A3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_3.setText(str('  ' + matriz[16][1]+ '  ' + matriz[16][0]))

		b = banderas(matriz[24][2])
		self.ui.label_A4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_4.setText(str('  ' + matriz[24][1]+ '  ' + matriz[24][0]))

		#Grupo B
		b = banderas(matriz[1][2])
		self.ui.label_B1.setStyleSheet(b.mostrar_bandera())
		self.ui.label_5.setText(str('  ' + matriz[1][1]+ '  ' + matriz[1][0]))

		b = banderas(matriz[9][2])
		self.ui.label_B2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_6.setText(str('  ' + matriz[9][1]+ '  ' + matriz[9][0]))

		b = banderas(matriz[17][2])
		self.ui.label_B3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_7.setText(str('  ' + matriz[17][1]+ '  ' + matriz[17][0]))

		b = banderas(matriz[25][2])
		self.ui.label_B4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_8.setText(str('  ' + matriz[25][1]+ '  ' + matriz[25][0]))
		
		#Grupo C
		b = banderas(matriz[2][2])
		self.ui.label_C1.setStyleSheet(b.mostrar_bandera())
		self.ui.label_9.setText(str('  ' + matriz[2][1]+ '  ' + matriz[2][0]))

		b = banderas(matriz[10][2])
		self.ui.label_C2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_10.setText(str('  ' + matriz[10][1]+ '  ' + matriz[10][0]))

		b = banderas(matriz[18][2])
		self.ui.label_C3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_11.setText(str('  ' + matriz[18][1]+ '  ' + matriz[18][0]))

		b = banderas(matriz[26][2])
		self.ui.label_C4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_12.setText(str('  ' + matriz[26][1]+ '  ' + matriz[26][0]))
		
		#Grupo D
		b = banderas(matriz[3][2])
		self.ui.label_D1.setStyleSheet(b.mostrar_bandera())
		self.ui.label_13.setText(str('  ' + matriz[3][1]+ '  ' + matriz[3][0]))

		b = banderas(matriz[11][2])
		self.ui.label_D2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_14.setText(str('  ' + matriz[11][1]+ '  ' + matriz[11][0]))

		b = banderas(matriz[19][2])
		self.ui.label_D3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_15.setText(str('  ' + matriz[19][1]+ '  ' + matriz[19][0]))

		b = banderas(matriz[27][2])
		self.ui.label_D4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_16.setText(str('  ' + matriz[27][1]+ '  ' + matriz[27][0]))

		#Grupo E
		b = banderas(matriz[4][2])
		self.ui.label_E1.setStyleSheet(b.mostrar_bandera())
		self.ui.label_17.setText(str('  ' + matriz[4][1]+ '  ' + matriz[4][0]))

		b = banderas(matriz[12][2])
		self.ui.label_E2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_18.setText(str('  ' + matriz[12][1]+ '  ' + matriz[12][0]))

		b = banderas(matriz[20][2])
		self.ui.label_E3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_19.setText(str('  ' + matriz[20][1]+ '  ' + matriz[20][0]))

		b = banderas(matriz[28][2])
		self.ui.label_E4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_20.setText(str('  ' + matriz[28][1]+ '  ' + matriz[28][0]))
		
		#Grupo F
		b = banderas(matriz[5][2])
		self.ui.label_F1.setStyleSheet(b.mostrar_bandera())
		self.ui.label_21.setText(str('  ' + matriz[5][1]+ '  ' + matriz[5][0]))

		b = banderas(matriz[13][2])
		self.ui.label_F2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_22.setText(str('  ' + matriz[13][1]+ '  ' + matriz[13][0]))

		b = banderas(matriz[21][2])
		self.ui.label_F3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_23.setText(str('  ' + matriz[21][1]+ '  ' + matriz[21][0]))

		b = banderas(matriz[29][2])
		self.ui.label_F4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_24.setText(str('  ' + matriz[29][1]+ '  ' + matriz[29][0]))

		#Grupo G
		b = banderas(matriz[6][2])
		self.ui.label_G1.setStyleSheet(b.mostrar_bandera())
		self.ui.label_25.setText(str('  ' + matriz[6][1]+ '  ' + matriz[6][0]))

		b = banderas(matriz[14][2])
		self.ui.label_G2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_26.setText(str('  ' + matriz[14][1]+ '  ' + matriz[14][0]))

		b = banderas(matriz[22][2])
		self.ui.label_G3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_27.setText(str('  ' + matriz[22][1]+ '  ' + matriz[22][0]))

		b = banderas(matriz[30][2])
		self.ui.label_G4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_28.setText(str('  ' + matriz[30][1]+ '  ' + matriz[30][0]))

		#Grupo H
		b = banderas(matriz[7][2])
		self.ui.label_H1.setStyleSheet(b.mostrar_bandera())
		self.ui.label_29.setText(str('  ' + matriz[7][1]+ '  ' + matriz[7][0]))

		b = banderas(matriz[15][2])
		self.ui.label_H2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_30.setText(str('  ' + matriz[15][1]+ '  ' + matriz[15][0]))

		b = banderas(matriz[23][2])
		self.ui.label_H3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_31.setText(str('  ' + matriz[23][1]+ '  ' + matriz[23][0]))
		
		b = banderas(matriz[31][2])
		self.ui.label_H4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_32.setText(str('  ' + matriz[31][1]+ '  ' + matriz[31][0]))

		self.ui.pushButton_sig.clicked.connect(self.sorteos)

		self.ui.pushButton.clicked.connect(self.resultadoA)
		self.ui.pushButton_2.clicked.connect(self.resultadoB)
		self.ui.pushButton_3.clicked.connect(self.resultadoC)
		self.ui.pushButton_4.clicked.connect(self.resultadoD)
		self.ui.pushButton_5.clicked.connect(self.resultadoE)
		self.ui.pushButton_6.clicked.connect(self.resultadoF)
		self.ui.pushButton_7.clicked.connect(self.resultadoG)
		self.ui.pushButton_8.clicked.connect(self.resultadoH)

	def sorteos (self):
		self.ventana = QtWidgets.QMainWindow()
		self.ui = Ui_sorteos()
		self.ui.setupUi(self.ventana)
		self.ventana.show() #Para ver

		global primeros, segundos

		for p in primeros:
			print("primero de grupo ", p)
			print(p[0])

		for s in segundos:
			print("Segundo de grupo ",s)

		
		if path.exists("octavos.txt"):
			fic = open("octavos.txt","r")
			lines = fic.readline()
			datos = []

			for j in range(0,8):
				datos = lines.split()
				print("datos", datos)
				primeros.append(datos)
				lines = fic.readline()
			for j in range(0,8):
				datos = lines.split()
				segundos.append(datos)
				lines = fic.readline()
			fic.close()

		if path.exists("octavos.txt") == False:
			print("hola")
			f = open('octavos.txt', 'w')

			for i in primeros:
				for j in range(0,3):
					f.write( i[j] + ' ')
				f.write('\n')
			for i in segundos:
				for j in range(0,3):
					f.write( i[j] + ' ')
				f.write('\n')
			f.close()

		self.mostrar()
		self.ui.sorteo.clicked.connect(self.octavos)

	def mostrar(self):
		#grupo A
		b = banderas(primeros[0][2])
		self.ui.label_A1.setStyleSheet(b.mostrar_bandera())
		self.ui.label_1.setText(str('  ' + primeros[0][1]+ '  ' + primeros[0][0]))

		b = banderas(segundos[0][2])
		self.ui.label_A1_3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_9.setText(str('  ' + segundos[0][1]+ '  ' + segundos[0][0]))

		#grupo B
		b = banderas(primeros[1][2])
		self.ui.label_A2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_2.setText(str('  ' + primeros[1][1]+ '  ' + primeros[1][0]))

		b = banderas(segundos[1][2])
		self.ui.label_A2_3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_10.setText(str('  ' + segundos[1][1]+ '  ' + segundos[1][0]))

		#grupo C
		b = banderas(primeros[2][2])
		self.ui.label_A3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_3.setText(str('  ' + primeros[2][1]+ '  ' + primeros[2][0]))

		b = banderas(segundos[2][2])
		self.ui.label_A3_3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_11.setText(str('  ' + segundos[2][1]+ '  ' + segundos[2][0]))

		#grupo D
		b = banderas(primeros[3][2])
		self.ui.label_A4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_4.setText(str('  ' + primeros[3][1]+ '  ' + primeros[3][0]))
		b = banderas(segundos[3][2])
		self.ui.label_A4_3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_12.setText(str('  ' + segundos[3][1]+ '  ' + segundos[3][0]))

		#Grupo E
		b = banderas(primeros[4][2])
		self.ui.label_A1_2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_5.setText(str('  ' + primeros[4][1]+ '  ' + primeros[4][0]))
		b = banderas(segundos[4][2])
		self.ui.label_A1_4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_13.setText(str('  ' + segundos[4][1]+ '  ' + segundos[4][0]))

		#Grupo F
		b = banderas(primeros[5][2])
		self.ui.label_A2_2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_6.setText(str('  ' + primeros[5][1]+ '  ' + primeros[5][0]))
		b = banderas(segundos[5][2])
		self.ui.label_A2_4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_14.setText(str('  ' + segundos[5][1]+ '  ' + segundos[5][0]))

		#Grupo G
		b = banderas(primeros[6][2])
		self.ui.label_A3_2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_7.setText(str('  ' + primeros[6][1]+ '  ' + primeros[6][0]))
		b = banderas(segundos[6][2])
		self.ui.label_A3_4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_15.setText(str('  ' + segundos[6][1]+ '  ' + segundos[6][0]))
		
		#Grupo H
		b = banderas(primeros[7][2])
		self.ui.label_A4_2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_8.setText(str('  ' + primeros[7][1]+ '  ' + primeros[7][0]))
		b = banderas(segundos[7][2])
		self.ui.label_A4_4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_16.setText(str('  ' + segundos[7][1]+ '  ' + segundos[7][0]))

	def octavos (self):
		self.ventana = QtWidgets.QMainWindow()
		self.ui = Ui_Octavos()
		self.ui.setupUi(self.ventana)
		self.ventana.show() #Para ver

		global primeros,segundos
 
		copia =[]
		copia2 = []

		for p in range(0,8):
			random.shuffle(primeros)
			copia.append(primeros.pop())
		for p in range(0,8):
			random.shuffle(segundos)
			copia2.append(segundos.pop())

		primeros = copia
		segundos = copia2
		self.mostrar()

		self.btngroup1 = QButtonGroup()
		self.btngroup2 = QButtonGroup()
		self.btngroup3 = QButtonGroup()
		self.btngroup4 = QButtonGroup()
		self.btngroup5 = QButtonGroup()
		self.btngroup6 = QButtonGroup()
		self.btngroup7 = QButtonGroup()
		self.btngroup8 = QButtonGroup()


		self.btngroup1.addButton(self.ui.radioButton)
		self.btngroup1.addButton(self.ui.radioButton_9)

		self.btngroup2.addButton(self.ui.radioButton_2)
		self.btngroup2.addButton(self.ui.radioButton_10)

		self.btngroup3.addButton(self.ui.radioButton_3)
		self.btngroup3.addButton(self.ui.radioButton_11)

		self.btngroup4.addButton(self.ui.radioButton_4)
		self.btngroup4.addButton(self.ui.radioButton_12)

		self.btngroup5.addButton(self.ui.radioButton_5)
		self.btngroup5.addButton(self.ui.radioButton_13)

		self.btngroup6.addButton(self.ui.radioButton_6)
		self.btngroup6.addButton(self.ui.radioButton_14)

		self.btngroup7.addButton(self.ui.radioButton_7)
		self.btngroup7.addButton(self.ui.radioButton_15)

		self.btngroup8.addButton(self.ui.radioButton_8)
		self.btngroup8.addButton(self.ui.radioButton_16)

		self.ui.pushButton_sig.clicked.connect(self.cuartos)

	def cuartos (self):

		self.ganadores()

		self.ventana = QtWidgets.QMainWindow()
		self.ui = Ui_Cuartos()
		self.ui.setupUi(self.ventana)
		self.ventana.show() #Para ver

		global cuartos
		copia = []

		for p in range(0,8):
			random.shuffle(cuartos)
			copia.append(cuartos.pop())
		cuartos = copia

		b = banderas(cuartos[0][2])
		self.ui.label_A1.setStyleSheet(b.mostrar_bandera())
		self.ui.label_1.setText(str('  ' + cuartos[0][1]+ '  ' + cuartos[0][0]))

		b = banderas(cuartos[1][2])
		self.ui.label_A2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_2.setText(str('  ' + cuartos[1][1]+ '  ' + cuartos[1][0]))
	
		b = banderas(cuartos[2][2])
		self.ui.label_A3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_3.setText(str('  ' + cuartos[2][1]+ '  ' + cuartos[2][0]))

		b = banderas(cuartos[3][2])
		self.ui.label_A4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_4.setText(str('  ' + cuartos[3][1]+ '  ' + cuartos[3][0]))
		
		b = banderas(cuartos[4][2])
		self.ui.label_A1_2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_5.setText(str('  ' + cuartos[4][1]+ '  ' + cuartos[4][0]))
		
		b = banderas(cuartos[5][2])
		self.ui.label_A2_2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_6.setText(str('  ' + cuartos[5][1]+ '  ' + cuartos[5][0]))
		
		b = banderas(cuartos[6][2])
		self.ui.label_A3_2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_7.setText(str('  ' + cuartos[6][1]+ '  ' + cuartos[6][0]))
		
		b = banderas(cuartos[7][2])
		self.ui.label_A4_2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_8.setText(str('  ' + cuartos[7][1]+ '  ' + cuartos[7][0]))
	
		self.btngroup1 = QButtonGroup()
		self.btngroup2 = QButtonGroup()
		self.btngroup3 = QButtonGroup()
		self.btngroup4 = QButtonGroup()


		self.btngroup1.addButton(self.ui.radioButton)
		self.btngroup1.addButton(self.ui.radioButton_2)

		self.btngroup2.addButton(self.ui.radioButton_3)
		self.btngroup2.addButton(self.ui.radioButton_4)

		self.btngroup3.addButton(self.ui.radioButton_5)
		self.btngroup3.addButton(self.ui.radioButton_6)

		self.btngroup4.addButton(self.ui.radioButton_7)
		self.btngroup4.addButton(self.ui.radioButton_8)

		self.ui.pushButton_sig.clicked.connect(self.decision)

	def decision(self):
		global band

		if band == 0:
			self.cuartos_final()
			band = 1
		elif band == 1:
			self.semifinal()
			band = 2
		elif band == 2:
			self.Campeon()
			band = 0

	def cuartos_final(self):

		global semifinal

		if self.ui.radioButton.isChecked():
			b = banderas(cuartos[0][2])
			self.ui.label_A1_3.setStyleSheet(b.mostrar_bandera())
			self.ui.label_9.setText(str('  ' + cuartos[0][1]+ '  ' + cuartos[0][0]))
			semifinal.append(cuartos[0])
		
		elif self.ui.radioButton_2.isChecked():
			b = banderas(cuartos[1][2])
			self.ui.label_A1_3.setStyleSheet(b.mostrar_bandera())
			self.ui.label_9.setText(str('  ' + cuartos[1][1]+ '  ' + cuartos[1][0]))
			semifinal.append(cuartos[1])
		
		if self.ui.radioButton_3.isChecked():
			b = banderas(cuartos[2][2])
			self.ui.label_A2_3.setStyleSheet(b.mostrar_bandera())
			self.ui.label_10.setText(str('  ' + cuartos[2][1]+ '  ' + cuartos[2][0]))
			semifinal.append(cuartos[2])
		
		elif self.ui.radioButton_4.isChecked():
			b = banderas(cuartos[3][2])
			self.ui.label_A2_3.setStyleSheet(b.mostrar_bandera())
			self.ui.label_10.setText(str('  ' + cuartos[3][1]+ '  ' + cuartos[3][0]))
			semifinal.append(cuartos[3])
			
		if self.ui.radioButton_5.isChecked():
			b = banderas(cuartos[4][2])
			self.ui.label_A3_3.setStyleSheet(b.mostrar_bandera())
			self.ui.label_11.setText(str('  ' + cuartos[4][1]+ '  ' + cuartos[4][0]))
			semifinal.append(cuartos[4])
		
		elif self.ui.radioButton_6.isChecked():
			b = banderas(cuartos[5][2])
			self.ui.label_A3_3.setStyleSheet(b.mostrar_bandera())
			self.ui.label_11.setText(str('  ' + cuartos[5][1]+ '  ' + cuartos[5][0]))
			semifinal.append(cuartos[5])

		if self.ui.radioButton_7.isChecked():
			b = banderas(cuartos[6][2])
			self.ui.label_A4_3.setStyleSheet(b.mostrar_bandera())
			self.ui.label_12.setText(str('  ' + cuartos[6][1]+ '  ' + cuartos[6][0]))
			semifinal.append(cuartos[6])
			
		elif self.ui.radioButton_8.isChecked():
			b = banderas(cuartos[7][2])
			self.ui.label_A4_3.setStyleSheet(b.mostrar_bandera())
			self.ui.label_12.setText(str('  ' + cuartos[7][1]+ '  ' + cuartos[7][0]))
			semifinal.append(cuartos[7])

		self.btngroupsemi = QButtonGroup()
		self.btngroupsemi2 = QButtonGroup()

		self.btngroupsemi.addButton(self.ui.radioButton_9)
		self.btngroupsemi.addButton(self.ui.radioButton_11)

		self.btngroupsemi2.addButton(self.ui.radioButton_10)
		self.btngroupsemi2.addButton(self.ui.radioButton_12)


	def semifinal(self):

		global semifinal
		global final

		for a in semifinal:
			print("semi", a)

		if self.ui.radioButton_9.isChecked():
			print("button9")
			b = banderas(semifinal[0][2])
			self.ui.label_A1_4.setStyleSheet(b.mostrar_bandera())
			self.ui.label_13.setText(str('  ' + semifinal[0][1]+ '  ' + semifinal[0][0]))
			final.append(semifinal[0])

		elif self.ui.radioButton_11.isChecked():
			print("button11")
			b = banderas(semifinal[2][2])
			self.ui.label_A1_4.setStyleSheet(b.mostrar_bandera())
			self.ui.label_13.setText(str('  ' + semifinal[2][1]+ '  ' + semifinal[2][0]))
			final.append(semifinal[2])

		if self.ui.radioButton_10.isChecked():
			print("button10")
			b = banderas(semifinal[1][2])
			self.ui.label_A2_4.setStyleSheet(b.mostrar_bandera())
			self.ui.label_14.setText(str('  ' + semifinal[1][1]+ '  ' + semifinal[1][0]))
			final.append(semifinal[1])

		elif self.ui.radioButton_12.isChecked():
			print("button12")
			b = banderas(semifinal[3][2])
			self.ui.label_A2_4.setStyleSheet(b.mostrar_bandera())
			self.ui.label_14.setText(str('  ' + semifinal[3][1]+ '  ' + semifinal[3][0]))
			final.append(semifinal[3])

		print("aqui voy")
		for b in final:
			print("final primer", b)

	def Campeon(self):
		global final

		print("print")

		for b in final:
			print("final", b)

		if self.ui.radioButton_13.isChecked():
			b = banderas(final[0][2])
			self.ui.label_campeon.setStyleSheet(b.mostrar_bandera())
			self.ui.label_campeon_2.setText(str('  ' + final[0][1]+ '  ' + final[0][0]))
			
		elif self.ui.radioButton_14.isChecked():
			b = banderas(final[1][2])
			self.ui.label_campeon.setStyleSheet(b.mostrar_bandera())
			self.ui.label_campeon_2.setText(str('  ' + final[1][1]+ '  ' + final[1][0]))

	def ganadores(self):

		global cuartos

		if self.ui.radioButton.isChecked():
			cuartos.append(primeros[0])
		elif self.ui.radioButton_9.isChecked():
			cuartos.append(segundos[0])

		if self.ui.radioButton_2.isChecked():
			cuartos.append(primeros[1])
		elif self.ui.radioButton_10.isChecked():
			cuartos.append(segundos[1])

		if self.ui.radioButton_3.isChecked():
			cuartos.append(primeros[2])
		elif self.ui.radioButton_11.isChecked():
			cuartos.append(segundos[2])

		if self.ui.radioButton_4.isChecked():
			cuartos.append(primeros[3])
		elif self.ui.radioButton_12.isChecked():
			cuartos.append(segundos[3])

		if self.ui.radioButton_5.isChecked():
			cuartos.append(primeros[4])
		elif self.ui.radioButton_13.isChecked():
			cuartos.append(segundos[4])

		if self.ui.radioButton_6.isChecked():
			cuartos.append(primeros[5])
		elif self.ui.radioButton_14.isChecked():
			cuartos.append(segundos[5])

		if self.ui.radioButton_7.isChecked():
			cuartos.append(primeros[6])
		elif self.ui.radioButton_15.isChecked():
			cuartos.append(segundos[6])

		if self.ui.radioButton_8.isChecked():
			cuartos.append(primeros[7])
		elif self.ui.radioButton_16.isChecked():
			cuartos.append(segundos[7])

	def resultadoA (self):

		self.ventana_2 = QtWidgets.QMainWindow()
		self.ui = Ui_ResultadoA()
		self.ui.setupUi(self.ventana_2)
		self.ventana_2.show() #Para ver

		b = banderas(matriz[0][2])
		self.ui.label_1.setStyleSheet(b.mostrar_bandera())
		self.ui.label_1_1.setText(str('  ' + matriz[0][1]+ '  ' + matriz[0][0]))

		b = banderas(matriz[8][2])
		self.ui.label_2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_2_2.setText(str('  ' + matriz[8][1]+ '  ' + matriz[8][0]))

		b = banderas(matriz[16][2])
		self.ui.label_3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_3_3.setText(str('  ' + matriz[16][1]+ '  ' + matriz[16][0]))

		b = banderas(matriz[24][2])
		self.ui.label_4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_4_4.setText(str('  ' + matriz[24][1]+ '  ' + matriz[24][0]))

		if path.exists("resultadosA.txt"):
			puntos = []
			fic = open("resultadosA.txt","r")
			lines = fic.readline()

			for j in range(0,4):
				puntos_jug = lines.split()
				for i in puntos_jug:
					puntos.append(i)
				lines = fic.readline()
	
			fic.close()

			self.ui.lineEdit_2_1.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_1.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_1.setText(str(puntos.pop(0)))
			self.ui.resultado1.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_2.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_2.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_2.setText(str(puntos.pop(0)))
			self.ui.resultado2.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_3.setText(str(puntos.pop(0)))
			self.ui.lineEdit_2_3.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_3.setText(str(puntos.pop(0)))
			self.ui.resultado3.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_4.setText(str(puntos.pop(0)))
			self.ui.lineEdit_2_4.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_4.setText(str(puntos.pop(0)))
			self.ui.resultado4.setText(str(puntos.pop(0)))


		self.ui.refrescar.clicked.connect(self.cuentaA)

	def cuentaA (self):

		#Revisa el archivo para cargar los datos

		#Fila 1
		lista1 = []

		if not self.ui.lineEdit_2_1.text():
			r2_1 = 0
		else:
			r2_1 = int(self.ui.lineEdit_2_1.text())
		
		if not self.ui.lineEdit_3_1.text():
			r3_1 = 0
		else:
			r3_1 = int(self.ui.lineEdit_3_1.text())

		if not self.ui.lineEdit_4_1.text():
			r4_1 = 0
		else:
			r4_1 = int(self.ui.lineEdit_4_1.text()) 
		
		puntos_r1 = r2_1 + r3_1 + r4_1
		lista1.append(str(r2_1))
		lista1.append(str(r3_1))
		lista1.append(str(r4_1))
		lista1.append(str(puntos_r1))

		self.ui.resultado1.setText(str(puntos_r1))

		#Fila 2
		lista2 = []

		if not self.ui.lineEdit_1_2.text():
			r1_2 = 0
		else:
			r1_2 = int(self.ui.lineEdit_1_2.text())
		
		if not self.ui.lineEdit_3_2.text():
			r3_2 = 0
		else:
			r3_2 = int(self.ui.lineEdit_3_2.text())

		if not self.ui.lineEdit_4_2.text():
			r4_2 = 0
		else:
			r4_2 = int(self.ui.lineEdit_4_2.text()) 
		
		puntos_r2 = r1_2 + r3_2 + r4_2

		lista2.append(str(r1_2))
		lista2.append(str(r3_2))
		lista2.append(str(r4_2))
		lista2.append(str(puntos_r2))

		self.ui.resultado2.setText(str(puntos_r2))

		#Fila 3
		lista3 = []

		if not self.ui.lineEdit_1_3.text():
			r1_3 = 0
		else:
			r1_3 = int(self.ui.lineEdit_1_3.text())
		
		if not self.ui.lineEdit_2_3.text():
			r2_3 = 0
		else:
			r2_3 = int(self.ui.lineEdit_2_3.text())

		if not self.ui.lineEdit_4_3.text():
			r4_3 = 0
		else:
			r4_3 = int(self.ui.lineEdit_4_3.text()) 
		
		puntos_r3 = r1_3 + r2_3 + r4_3

		lista3.append(str(r1_3))
		lista3.append(str(r2_3))
		lista3.append(str(r4_3))
		lista3.append(str(puntos_r3))

		self.ui.resultado3.setText(str(puntos_r3))

		#Fila 4
		lista4 = []

		if not self.ui.lineEdit_1_4.text():
			r1_4 = 0
		else:
			r1_4 = int(self.ui.lineEdit_1_4.text())
		
		if not self.ui.lineEdit_2_4.text():
			r2_4 = 0
		else:
			r2_4 = int(self.ui.lineEdit_2_4.text())

		if not self.ui.lineEdit_3_4.text():
			r3_4 = 0
		else:
			r3_4 = int(self.ui.lineEdit_3_4.text()) 
		
		puntos_r4 = r1_4 + r2_4 + r3_4

		lista4.append(str(r1_4))
		lista4.append(str(r2_4))
		lista4.append(str(r3_4))
		lista4.append(str(puntos_r4))

		self.ui.resultado4.setText(str(puntos_r4))

		f = open('resultadosA.txt', 'w')

		for i in lista1:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista2:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista3:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista4:
			f.write( i + ' ')
		f.write('\n')	

		f.write("-------------" + '\n')

		f.close()

		# Primero y Segundo
		clasificacion = []
		clasificacion.append(int(lista1[3]))
		clasificacion.append(int(lista2[3]))
		clasificacion.append(int(lista3[3]))
		clasificacion.append(int(lista4[3]))

		#ordenamiento de mayor a menor
		for j in clasificacion:
			for i in range(0,3):
				if clasificacion[i] < clasificacion[i+1]:
					aux = clasificacion[i]
					clasificacion[i] = clasificacion[i+1]
					clasificacion[i+1] = aux

		if str(clasificacion[0]) == lista1[3]:
			primero = matriz[0]
			if str(clasificacion[1]) ==lista2[3]:
				segundo = matriz[8]
			elif str(clasificacion[1]) == lista3[3]:
				segundo = matriz[16]
			else:
				segundo = matriz[24]

		elif str(clasificacion[0]) == lista2[3]:
			primero = matriz[8]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[0]
			elif str(clasificacion[1]) ==lista3[3]:
				segundo = matriz[16]
			else:
				segundo = matriz[24]

		elif str(clasificacion[0]) == lista3[3]:
			primero = matriz[16]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[0]
			elif str(clasificacion[1]) == lista2[3]:
				segundo = matriz[8]
			else:
				segundo = matriz[24]

		else:
			primero = matriz[24]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[10]
			elif str(clasificacion[1]) == lista2[3]:
				segundo = matriz[8]
			else:
				segundo = matriz[16]

		print("primero", primero)
		print("segundo", segundo)

		primeros.insert(0,primero)
		segundos.insert(0,segundo)

	def resultadoB (self):
		self.ventana_2 = QtWidgets.QMainWindow()
		self.ui = Ui_ResultadoB()
		self.ui.setupUi(self.ventana_2)
		self.ventana_2.show() #Para ver

		b = banderas(matriz[1][2])
		self.ui.label_1.setStyleSheet(b.mostrar_bandera())
		self.ui.label_1_1.setText(str('  ' + matriz[1][1]+ '  ' + matriz[1][0]))

		b = banderas(matriz[9][2])
		self.ui.label_2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_2_2.setText(str('  ' + matriz[9][1]+ '  ' + matriz[9][0]))

		b = banderas(matriz[17][2])
		self.ui.label_3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_3_3.setText(str('  ' + matriz[17][1]+ '  ' + matriz[17][0]))

		b = banderas(matriz[25][2])
		self.ui.label_4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_4_4.setText(str('  ' + matriz[25][1]+ '  ' + matriz[25][0]))

		if path.exists("resultadosB.txt"):
			puntos = []
			fic = open("resultadosB.txt","r")
			lines = fic.readline()

			for j in range(0,4):
				puntos_jug = lines.split()
				for i in puntos_jug:
					puntos.append(i)
				lines = fic.readline()
	
			fic.close()

			self.ui.lineEdit_2_1.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_1.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_1.setText(str(puntos.pop(0)))
			self.ui.resultado1.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_2.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_2.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_2.setText(str(puntos.pop(0)))
			self.ui.resultado2.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_3.setText(str(puntos.pop(0)))
			self.ui.lineEdit_2_3.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_3.setText(str(puntos.pop(0)))
			self.ui.resultado3.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_4.setText(str(puntos.pop(0)))
			self.ui.lineEdit_2_4.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_4.setText(str(puntos.pop(0)))
			self.ui.resultado4.setText(str(puntos.pop(0)))


		self.ui.refrescar.clicked.connect(self.cuentaB)

	def cuentaB (self):

		#Fila 1
		lista1 = []

		if not self.ui.lineEdit_2_1.text():
			r2_1 = 0
		else:
			r2_1 = int(self.ui.lineEdit_2_1.text())
		
		if not self.ui.lineEdit_3_1.text():
			r3_1 = 0
		else:
			r3_1 = int(self.ui.lineEdit_3_1.text())

		if not self.ui.lineEdit_4_1.text():
			r4_1 = 0
		else:
			r4_1 = int(self.ui.lineEdit_4_1.text()) 
		
		puntos_r1 = r2_1 + r3_1 + r4_1
		lista1.append(str(r2_1))
		lista1.append(str(r3_1))
		lista1.append(str(r4_1))
		lista1.append(str(puntos_r1))

		self.ui.resultado1.setText(str(puntos_r1))

		#Fila 2
		lista2 = []

		if not self.ui.lineEdit_1_2.text():
			r1_2 = 0
		else:
			r1_2 = int(self.ui.lineEdit_1_2.text())
		
		if not self.ui.lineEdit_3_2.text():
			r3_2 = 0
		else:
			r3_2 = int(self.ui.lineEdit_3_2.text())

		if not self.ui.lineEdit_4_2.text():
			r4_2 = 0
		else:
			r4_2 = int(self.ui.lineEdit_4_2.text()) 
		
		puntos_r2 = r1_2 + r3_2 + r4_2

		lista2.append(str(r1_2))
		lista2.append(str(r3_2))
		lista2.append(str(r4_2))
		lista2.append(str(puntos_r2))

		self.ui.resultado2.setText(str(puntos_r2))

		#Fila 3
		lista3 = []

		if not self.ui.lineEdit_1_3.text():
			r1_3 = 0
		else:
			r1_3 = int(self.ui.lineEdit_1_3.text())
		
		if not self.ui.lineEdit_2_3.text():
			r2_3 = 0
		else:
			r2_3 = int(self.ui.lineEdit_2_3.text())

		if not self.ui.lineEdit_4_3.text():
			r4_3 = 0
		else:
			r4_3 = int(self.ui.lineEdit_4_3.text()) 
		
		puntos_r3 = r1_3 + r2_3 + r4_3

		lista3.append(str(r1_3))
		lista3.append(str(r2_3))
		lista3.append(str(r4_3))
		lista3.append(str(puntos_r3))

		self.ui.resultado3.setText(str(puntos_r3))

		#Fila 4
		lista4 = []

		if not self.ui.lineEdit_1_4.text():
			r1_4 = 0
		else:
			r1_4 = int(self.ui.lineEdit_1_4.text())
		
		if not self.ui.lineEdit_2_4.text():
			r2_4 = 0
		else:
			r2_4 = int(self.ui.lineEdit_2_4.text())

		if not self.ui.lineEdit_3_4.text():
			r3_4 = 0
		else:
			r3_4 = int(self.ui.lineEdit_3_4.text()) 
		
		puntos_r4 = r1_4 + r2_4 + r3_4

		lista4.append(str(r1_4))
		lista4.append(str(r2_4))
		lista4.append(str(r3_4))
		lista4.append(str(puntos_r4))

		self.ui.resultado4.setText(str(puntos_r4))

		f = open('resultadosB.txt', 'w')

		for i in lista1:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista2:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista3:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista4:
			f.write( i + ' ')
		f.write('\n')	

		f.write("-------------" + '\n')

		f.close()

		# Primero y Segundo
		clasificacion = []
		clasificacion.append(int(lista1[3]))
		clasificacion.append(int(lista2[3]))
		clasificacion.append(int(lista3[3]))
		clasificacion.append(int(lista4[3]))

		#ordenamiento de mayor a menor
		for j in clasificacion:
			for i in range(0,3):
				if clasificacion[i] < clasificacion[i+1]:
					aux = clasificacion[i]
					clasificacion[i] = clasificacion[i+1]
					clasificacion[i+1] = aux

		if str(clasificacion[0]) == lista1[3]:
			primero = matriz[1]
			if str(clasificacion[1]) == lista2[3]:
				segundo = matriz[9]
			elif str(clasificacion[1]) == lista3[3]:
				segundo = matriz[17]
			else:
				segundo = matriz[25]

		elif str(clasificacion[0]) == lista2[3]:
			primero = matriz[9]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[1]
			elif str(clasificacion[1]) == lista3[3]:
				segundo = matriz[17]
			else:
				segundo = matriz[25]

		elif str(clasificacion[0]) == lista3[3]:
			primero = matriz[17]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[1]
			elif str(clasificacion[1]) == lista2[3]:
				segundo = matriz[9]
			else:
				segundo = matriz[25]

		else:
			primero = matriz[25]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[1]
			elif str(clasificacion[1]) == lista2[3]:
				segundo = matriz[9]
			else:
				segundo = matriz[17]

		print("primero", primero)
		print("segundo", segundo)
		
		primeros.insert(1,primero)
		segundos.insert(1,segundo)

	def resultadoC (self):
		self.ventana_2 = QtWidgets.QMainWindow()
		self.ui = Ui_ResultadoC()
		self.ui.setupUi(self.ventana_2)
		self.ventana_2.show() #Para ver

		b = banderas(matriz[2][2])
		self.ui.label_1.setStyleSheet(b.mostrar_bandera())
		self.ui.label_1_1.setText(str('  ' + matriz[2][1]+ '  ' + matriz[2][0]))

		b = banderas(matriz[10][2])
		self.ui.label_2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_2_2.setText(str('  ' + matriz[10][1]+ '  ' + matriz[10][0]))

		b = banderas(matriz[18][2])
		self.ui.label_3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_3_3.setText(str('  ' + matriz[18][1]+ '  ' + matriz[18][0]))

		b = banderas(matriz[26][2])
		self.ui.label_4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_4_4.setText(str('  ' + matriz[26][1]+ '  ' + matriz[26][0]))

		if path.exists("resultadosC.txt"):
			puntos = []
			fic = open("resultadosC.txt","r")
			lines = fic.readline()

			for j in range(0,4):
				puntos_jug = lines.split()
				for i in puntos_jug:
					puntos.append(i)
				lines = fic.readline()
	
			fic.close()

			self.ui.lineEdit_2_1.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_1.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_1.setText(str(puntos.pop(0)))
			self.ui.resultado1.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_2.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_2.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_2.setText(str(puntos.pop(0)))
			self.ui.resultado2.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_3.setText(str(puntos.pop(0)))
			self.ui.lineEdit_2_3.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_3.setText(str(puntos.pop(0)))
			self.ui.resultado3.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_4.setText(str(puntos.pop(0)))
			self.ui.lineEdit_2_4.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_4.setText(str(puntos.pop(0)))
			self.ui.resultado4.setText(str(puntos.pop(0)))

		self.ui.refrescar.clicked.connect(self.cuentaC)

	def cuentaC (self):

		#Fila 1
		lista1 = []

		if not self.ui.lineEdit_2_1.text():
			r2_1 = 0
		else:
			r2_1 = int(self.ui.lineEdit_2_1.text())
		
		if not self.ui.lineEdit_3_1.text():
			r3_1 = 0
		else:
			r3_1 = int(self.ui.lineEdit_3_1.text())

		if not self.ui.lineEdit_4_1.text():
			r4_1 = 0
		else:
			r4_1 = int(self.ui.lineEdit_4_1.text()) 
		
		puntos_r1 = r2_1 + r3_1 + r4_1
		lista1.append(str(r2_1))
		lista1.append(str(r3_1))
		lista1.append(str(r4_1))
		lista1.append(str(puntos_r1))

		self.ui.resultado1.setText(str(puntos_r1))

		#Fila 2
		lista2 = []

		if not self.ui.lineEdit_1_2.text():
			r1_2 = 0
		else:
			r1_2 = int(self.ui.lineEdit_1_2.text())
		
		if not self.ui.lineEdit_3_2.text():
			r3_2 = 0
		else:
			r3_2 = int(self.ui.lineEdit_3_2.text())

		if not self.ui.lineEdit_4_2.text():
			r4_2 = 0
		else:
			r4_2 = int(self.ui.lineEdit_4_2.text()) 
		
		puntos_r2 = r1_2 + r3_2 + r4_2

		lista2.append(str(r1_2))
		lista2.append(str(r3_2))
		lista2.append(str(r4_2))
		lista2.append(str(puntos_r2))

		self.ui.resultado2.setText(str(puntos_r2))

		#Fila 3
		lista3 = []

		if not self.ui.lineEdit_1_3.text():
			r1_3 = 0
		else:
			r1_3 = int(self.ui.lineEdit_1_3.text())
		
		if not self.ui.lineEdit_2_3.text():
			r2_3 = 0
		else:
			r2_3 = int(self.ui.lineEdit_2_3.text())

		if not self.ui.lineEdit_4_3.text():
			r4_3 = 0
		else:
			r4_3 = int(self.ui.lineEdit_4_3.text()) 
		
		puntos_r3 = r1_3 + r2_3 + r4_3

		lista3.append(str(r1_3))
		lista3.append(str(r2_3))
		lista3.append(str(r4_3))
		lista3.append(str(puntos_r3))

		self.ui.resultado3.setText(str(puntos_r3))

		#Fila 4
		lista4 = []

		if not self.ui.lineEdit_1_4.text():
			r1_4 = 0
		else:
			r1_4 = int(self.ui.lineEdit_1_4.text())
		
		if not self.ui.lineEdit_2_4.text():
			r2_4 = 0
		else:
			r2_4 = int(self.ui.lineEdit_2_4.text())

		if not self.ui.lineEdit_3_4.text():
			r3_4 = 0
		else:
			r3_4 = int(self.ui.lineEdit_3_4.text()) 
		
		puntos_r4 = r1_4 + r2_4 + r3_4

		lista4.append(str(r1_4))
		lista4.append(str(r2_4))
		lista4.append(str(r3_4))
		lista4.append(str(puntos_r4))

		self.ui.resultado4.setText(str(puntos_r4))

		f = open('resultadosC.txt', 'w')

		for i in lista1:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista2:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista3:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista4:
			f.write( i + ' ')
		f.write('\n')	

		f.write("-------------" + '\n')

		f.close()

		# Primero y Segundo
		clasificacion = []
		clasificacion.append(int(lista1[3]))
		clasificacion.append(int(lista2[3]))
		clasificacion.append(int(lista3[3]))
		clasificacion.append(int(lista4[3]))

		#ordenamiento de mayor a menor
		for j in clasificacion:
			for i in range(0,3):
				if clasificacion[i] < clasificacion[i+1]:
					aux = clasificacion[i]
					clasificacion[i] = clasificacion[i+1]
					clasificacion[i+1] = aux

		if str(clasificacion[0]) == lista1[3]:
			primero = matriz[2]
			if str(clasificacion[1]) == lista2[3]:
				segundo = matriz[10]
			elif str(clasificacion[1]) == lista3[3]:
				segundo = matriz[18]
			else:
				segundo = matriz[26]

		elif str(clasificacion[0]) == lista2[3]:
			primero = matriz[10]

			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[2]
			elif str(clasificacion[1]) == lista3[3]:
				segundo = matriz[18]
			else:
				segundo = matriz[26]

		elif str(clasificacion[0]) == lista3[3]:
			primero = matriz[18]

			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[2]
			elif str(clasificacion[1]) == lista2[3]:
				segundo = matriz[10]
			else:
				segundo = matriz[26]

		else:
			primero = matriz[26]

			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[2]
			elif str(clasificacion[1]) == lista2[3]:
				segundo = matriz[10]
			else:
				segundo = matriz[18]

		print("primero", primero)
		print("segundo", segundo)

		primeros.insert(2,primero)
		segundos.insert(2,segundo)

	def resultadoD (self):
		self.ventana_2 = QtWidgets.QMainWindow()
		self.ui = Ui_ResultadoD()
		self.ui.setupUi(self.ventana_2)
		self.ventana_2.show() #Para ver

		b = banderas(matriz[3][2])
		self.ui.label_1.setStyleSheet(b.mostrar_bandera())
		self.ui.label_1_1.setText(str('  ' + matriz[3][1]+ '  ' + matriz[3][0]))

		b = banderas(matriz[11][2])
		self.ui.label_2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_2_2.setText(str('  ' + matriz[11][1]+ '  ' + matriz[11][0]))

		b = banderas(matriz[19][2])
		self.ui.label_3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_3_3.setText(str('  ' + matriz[19][1]+ '  ' + matriz[19][0]))

		b = banderas(matriz[27][2])
		self.ui.label_4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_4_4.setText(str('  ' + matriz[27][1]+ '  ' + matriz[27][0]))

		if path.exists("resultadosD.txt"):
			puntos = []
			fic = open("resultadosD.txt","r")
			lines = fic.readline()

			for j in range(0,4):
				puntos_jug = lines.split()
				for i in puntos_jug:
					puntos.append(i)
				lines = fic.readline()
	
			fic.close()

			self.ui.lineEdit_2_1.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_1.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_1.setText(str(puntos.pop(0)))
			self.ui.resultado1.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_2.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_2.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_2.setText(str(puntos.pop(0)))
			self.ui.resultado2.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_3.setText(str(puntos.pop(0)))
			self.ui.lineEdit_2_3.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_3.setText(str(puntos.pop(0)))
			self.ui.resultado3.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_4.setText(str(puntos.pop(0)))
			self.ui.lineEdit_2_4.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_4.setText(str(puntos.pop(0)))
			self.ui.resultado4.setText(str(puntos.pop(0)))

		self.ui.refrescar.clicked.connect(self.cuentaD)

	def cuentaD (self):

		#Fila 1
		lista1 = []

		if not self.ui.lineEdit_2_1.text():
			r2_1 = 0
		else:
			r2_1 = int(self.ui.lineEdit_2_1.text())
		
		if not self.ui.lineEdit_3_1.text():
			r3_1 = 0
		else:
			r3_1 = int(self.ui.lineEdit_3_1.text())

		if not self.ui.lineEdit_4_1.text():
			r4_1 = 0
		else:
			r4_1 = int(self.ui.lineEdit_4_1.text()) 
		
		puntos_r1 = r2_1 + r3_1 + r4_1
		lista1.append(str(r2_1))
		lista1.append(str(r3_1))
		lista1.append(str(r4_1))
		lista1.append(str(puntos_r1))

		self.ui.resultado1.setText(str(puntos_r1))

		#Fila 2
		lista2 = []

		if not self.ui.lineEdit_1_2.text():
			r1_2 = 0
		else:
			r1_2 = int(self.ui.lineEdit_1_2.text())
		
		if not self.ui.lineEdit_3_2.text():
			r3_2 = 0
		else:
			r3_2 = int(self.ui.lineEdit_3_2.text())

		if not self.ui.lineEdit_4_2.text():
			r4_2 = 0
		else:
			r4_2 = int(self.ui.lineEdit_4_2.text()) 
		
		puntos_r2 = r1_2 + r3_2 + r4_2

		lista2.append(str(r1_2))
		lista2.append(str(r3_2))
		lista2.append(str(r4_2))
		lista2.append(str(puntos_r2))

		self.ui.resultado2.setText(str(puntos_r2))

		#Fila 3
		lista3 = []

		if not self.ui.lineEdit_1_3.text():
			r1_3 = 0
		else:
			r1_3 = int(self.ui.lineEdit_1_3.text())
		
		if not self.ui.lineEdit_2_3.text():
			r2_3 = 0
		else:
			r2_3 = int(self.ui.lineEdit_2_3.text())

		if not self.ui.lineEdit_4_3.text():
			r4_3 = 0
		else:
			r4_3 = int(self.ui.lineEdit_4_3.text()) 
		
		puntos_r3 = r1_3 + r2_3 + r4_3

		lista3.append(str(r1_3))
		lista3.append(str(r2_3))
		lista3.append(str(r4_3))
		lista3.append(str(puntos_r3))

		self.ui.resultado3.setText(str(puntos_r3))

		#Fila 4
		lista4 = []

		if not self.ui.lineEdit_1_4.text():
			r1_4 = 0
		else:
			r1_4 = int(self.ui.lineEdit_1_4.text())
		
		if not self.ui.lineEdit_2_4.text():
			r2_4 = 0
		else:
			r2_4 = int(self.ui.lineEdit_2_4.text())

		if not self.ui.lineEdit_3_4.text():
			r3_4 = 0
		else:
			r3_4 = int(self.ui.lineEdit_3_4.text()) 
		
		puntos_r4 = r1_4 + r2_4 + r3_4

		lista4.append(str(r1_4))
		lista4.append(str(r2_4))
		lista4.append(str(r3_4))
		lista4.append(str(puntos_r4))

		self.ui.resultado4.setText(str(puntos_r4))

		f = open('resultadosD.txt', 'w')

		for i in lista1:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista2:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista3:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista4:
			f.write( i + ' ')
		f.write('\n')	

		f.write("-------------" + '\n')

		f.close()

		# Primero y Segundo
		clasificacion = []
		clasificacion.append(int(lista1[3]))
		clasificacion.append(int(lista2[3]))
		clasificacion.append(int(lista3[3]))
		clasificacion.append(int(lista4[3]))

		#ordenamiento de mayor a menor
		for j in clasificacion:
			for i in range(0,3):
				if clasificacion[i] < clasificacion[i+1]:
					aux = clasificacion[i]
					clasificacion[i] = clasificacion[i+1]
					clasificacion[i+1] = aux

		if str(clasificacion[0]) == lista1[3]:
			primero = matriz[3]
			if str(clasificacion[1]) == lista2[3]:
				segundo = matriz[11]
			elif str(clasificacion[1]) == lista3[3]:
				segundo = matriz[19]
			else:
				segundo = matriz[27]

		elif str(clasificacion[0]) == lista2[3]:
			primero = matriz[11]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[3]
			elif str(clasificacion[1]) == lista3[3]:
				segundo = matriz[19]
			else:
				segundo = matriz[27]

		elif str(clasificacion[0]) == lista3[3]:
			primero = matriz[19]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[3]
			elif str(clasificacion[1]) == lista2[3]:
				segundo = matriz[11]
			else:
				segundo = matriz[27]

		else:
			primero = matriz[27]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[3]
			elif str(clasificacion[1]) == lista2[3]:
				segundo = matriz[11]
			else:
				segundo = matriz[19]

		print("primero", primero)
		print("segundo", segundo)
		primeros.insert(3,primero)
		segundos.insert(3,segundo)

	def resultadoE (self):
		self.ventana_2 = QtWidgets.QMainWindow()
		self.ui = Ui_ResultadoE()
		self.ui.setupUi(self.ventana_2)
		self.ventana_2.show() #Para ver

		b = banderas(matriz[4][2])
		self.ui.label_1.setStyleSheet(b.mostrar_bandera())
		self.ui.label_1_1.setText(str('  ' + matriz[4][1]+ '  ' + matriz[4][0]))

		b = banderas(matriz[12][2])
		self.ui.label_2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_2_2.setText(str('  ' + matriz[12][1]+ '  ' + matriz[12][0]))

		b = banderas(matriz[20][2])
		self.ui.label_3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_3_3.setText(str('  ' + matriz[20][1]+ '  ' + matriz[20][0]))

		b = banderas(matriz[28][2])
		self.ui.label_4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_4_4.setText(str('  ' + matriz[28][1]+ '  ' + matriz[28][0]))

		if path.exists("resultadosE.txt"):
			puntos = []
			fic = open("resultadosE.txt","r")
			lines = fic.readline()

			for j in range(0,4):
				puntos_jug = lines.split()
				for i in puntos_jug:
					puntos.append(i)
				lines = fic.readline()
	
			fic.close()

			self.ui.lineEdit_2_1.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_1.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_1.setText(str(puntos.pop(0)))
			self.ui.resultado1.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_2.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_2.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_2.setText(str(puntos.pop(0)))
			self.ui.resultado2.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_3.setText(str(puntos.pop(0)))
			self.ui.lineEdit_2_3.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_3.setText(str(puntos.pop(0)))
			self.ui.resultado3.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_4.setText(str(puntos.pop(0)))
			self.ui.lineEdit_2_4.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_4.setText(str(puntos.pop(0)))
			self.ui.resultado4.setText(str(puntos.pop(0)))

		self.ui.refrescar.clicked.connect(self.cuentaE)

	def cuentaE (self):

		#Fila 1
		lista1 = []

		if not self.ui.lineEdit_2_1.text():
			r2_1 = 0
		else:
			r2_1 = int(self.ui.lineEdit_2_1.text())
		
		if not self.ui.lineEdit_3_1.text():
			r3_1 = 0
		else:
			r3_1 = int(self.ui.lineEdit_3_1.text())

		if not self.ui.lineEdit_4_1.text():
			r4_1 = 0
		else:
			r4_1 = int(self.ui.lineEdit_4_1.text()) 
		
		puntos_r1 = r2_1 + r3_1 + r4_1
		lista1.append(str(r2_1))
		lista1.append(str(r3_1))
		lista1.append(str(r4_1))
		lista1.append(str(puntos_r1))

		self.ui.resultado1.setText(str(puntos_r1))

		#Fila 2
		lista2 = []

		if not self.ui.lineEdit_1_2.text():
			r1_2 = 0
		else:
			r1_2 = int(self.ui.lineEdit_1_2.text())
		
		if not self.ui.lineEdit_3_2.text():
			r3_2 = 0
		else:
			r3_2 = int(self.ui.lineEdit_3_2.text())

		if not self.ui.lineEdit_4_2.text():
			r4_2 = 0
		else:
			r4_2 = int(self.ui.lineEdit_4_2.text()) 
		
		puntos_r2 = r1_2 + r3_2 + r4_2

		lista2.append(str(r1_2))
		lista2.append(str(r3_2))
		lista2.append(str(r4_2))
		lista2.append(str(puntos_r2))

		self.ui.resultado2.setText(str(puntos_r2))

		#Fila 3
		lista3 = []

		if not self.ui.lineEdit_1_3.text():
			r1_3 = 0
		else:
			r1_3 = int(self.ui.lineEdit_1_3.text())
		
		if not self.ui.lineEdit_2_3.text():
			r2_3 = 0
		else:
			r2_3 = int(self.ui.lineEdit_2_3.text())

		if not self.ui.lineEdit_4_3.text():
			r4_3 = 0
		else:
			r4_3 = int(self.ui.lineEdit_4_3.text()) 
		
		puntos_r3 = r1_3 + r2_3 + r4_3

		lista3.append(str(r1_3))
		lista3.append(str(r2_3))
		lista3.append(str(r4_3))
		lista3.append(str(puntos_r3))

		self.ui.resultado3.setText(str(puntos_r3))

		#Fila 4
		lista4 = []

		if not self.ui.lineEdit_1_4.text():
			r1_4 = 0
		else:
			r1_4 = int(self.ui.lineEdit_1_4.text())
		
		if not self.ui.lineEdit_2_4.text():
			r2_4 = 0
		else:
			r2_4 = int(self.ui.lineEdit_2_4.text())

		if not self.ui.lineEdit_3_4.text():
			r3_4 = 0
		else:
			r3_4 = int(self.ui.lineEdit_3_4.text()) 
		
		puntos_r4 = r1_4 + r2_4 + r3_4

		lista4.append(str(r1_4))
		lista4.append(str(r2_4))
		lista4.append(str(r3_4))
		lista4.append(str(puntos_r4))

		self.ui.resultado4.setText(str(puntos_r4))

		f = open('resultadosE.txt', 'w')

		for i in lista1:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista2:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista3:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista4:
			f.write( i + ' ')
		f.write('\n')	

		f.write("-------------" + '\n')

		f.close()

		# Primero y Segundo
		clasificacion = []
		clasificacion.append(int(lista1[3]))
		clasificacion.append(int(lista2[3]))
		clasificacion.append(int(lista3[3]))
		clasificacion.append(int(lista4[3]))

		#ordenamiento de mayor a menor
		for j in clasificacion:
			for i in range(0,3):
				if clasificacion[i] < clasificacion[i+1]:
					aux = clasificacion[i]
					clasificacion[i] = clasificacion[i+1]
					clasificacion[i+1] = aux

		if str(clasificacion[0]) == lista1[3]:
			primero = matriz[4]
			if str(clasificacion[1]) == lista2[3]:
				segundo = matriz[12]
			elif str(clasificacion[1]) == lista3[3]:
				segundo = matriz[20]
			else:
				segundo = matriz[28]

		elif str(clasificacion[0]) == lista2[3]:
			primero = matriz[12]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[4]
			elif str(clasificacion[1]) == lista3[3]:
				segundo = matriz[17]
			else:
				segundo = matriz[28]

		elif str(clasificacion[0]) == lista3[3]:
			primero = matriz[20]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[4]
			elif str(clasificacion[1]) == lista2[3]:
				segundo = matriz[12]
			else:
				segundo = matriz[28]

		else:
			primero = matriz[28]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[4]
			elif str(clasificacion[1]) == lista2[3]:
				segundo = matriz[12]
			else:
				segundo = matriz[20]

		print("primero", primero)
		print("segundo", segundo)
		primeros.insert(4,primero)
		segundos.insert(4,segundo)

	def resultadoF (self):
		self.ventana_2 = QtWidgets.QMainWindow()
		self.ui = Ui_ResultadoF()
		self.ui.setupUi(self.ventana_2)
		self.ventana_2.show() #Para ver

		b = banderas(matriz[5][2])
		self.ui.label_1.setStyleSheet(b.mostrar_bandera())
		self.ui.label_1_1.setText(str('  ' + matriz[5][1]+ '  ' + matriz[5][0]))

		b = banderas(matriz[13][2])
		self.ui.label_2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_2_2.setText(str('  ' + matriz[13][1]+ '  ' + matriz[13][0]))

		b = banderas(matriz[21][2])
		self.ui.label_3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_3_3.setText(str('  ' + matriz[21][1]+ '  ' + matriz[21][0]))

		b = banderas(matriz[29][2])
		self.ui.label_4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_4_4.setText(str('  ' + matriz[29][1]+ '  ' + matriz[29][0]))

		if path.exists("resultadosF.txt"):
			puntos = []
			fic = open("resultadosF.txt","r")
			lines = fic.readline()

			for j in range(0,4):
				puntos_jug = lines.split()
				for i in puntos_jug:
					puntos.append(i)
				lines = fic.readline()
	
			fic.close()

			self.ui.lineEdit_2_1.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_1.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_1.setText(str(puntos.pop(0)))
			self.ui.resultado1.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_2.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_2.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_2.setText(str(puntos.pop(0)))
			self.ui.resultado2.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_3.setText(str(puntos.pop(0)))
			self.ui.lineEdit_2_3.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_3.setText(str(puntos.pop(0)))
			self.ui.resultado3.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_4.setText(str(puntos.pop(0)))
			self.ui.lineEdit_2_4.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_4.setText(str(puntos.pop(0)))
			self.ui.resultado4.setText(str(puntos.pop(0)))

		self.ui.refrescar.clicked.connect(self.cuentaF)

	def cuentaF (self):

		#Fila 1
		lista1 = []

		if not self.ui.lineEdit_2_1.text():
			r2_1 = 0
		else:
			r2_1 = int(self.ui.lineEdit_2_1.text())
		
		if not self.ui.lineEdit_3_1.text():
			r3_1 = 0
		else:
			r3_1 = int(self.ui.lineEdit_3_1.text())

		if not self.ui.lineEdit_4_1.text():
			r4_1 = 0
		else:
			r4_1 = int(self.ui.lineEdit_4_1.text()) 
		
		puntos_r1 = r2_1 + r3_1 + r4_1
		lista1.append(str(r2_1))
		lista1.append(str(r3_1))
		lista1.append(str(r4_1))
		lista1.append(str(puntos_r1))

		self.ui.resultado1.setText(str(puntos_r1))

		#Fila 2
		lista2 = []

		if not self.ui.lineEdit_1_2.text():
			r1_2 = 0
		else:
			r1_2 = int(self.ui.lineEdit_1_2.text())
		
		if not self.ui.lineEdit_3_2.text():
			r3_2 = 0
		else:
			r3_2 = int(self.ui.lineEdit_3_2.text())

		if not self.ui.lineEdit_4_2.text():
			r4_2 = 0
		else:
			r4_2 = int(self.ui.lineEdit_4_2.text()) 
		
		puntos_r2 = r1_2 + r3_2 + r4_2

		lista2.append(str(r1_2))
		lista2.append(str(r3_2))
		lista2.append(str(r4_2))
		lista2.append(str(puntos_r2))

		self.ui.resultado2.setText(str(puntos_r2))

		#Fila 3
		lista3 = []

		if not self.ui.lineEdit_1_3.text():
			r1_3 = 0
		else:
			r1_3 = int(self.ui.lineEdit_1_3.text())
		
		if not self.ui.lineEdit_2_3.text():
			r2_3 = 0
		else:
			r2_3 = int(self.ui.lineEdit_2_3.text())

		if not self.ui.lineEdit_4_3.text():
			r4_3 = 0
		else:
			r4_3 = int(self.ui.lineEdit_4_3.text()) 
		
		puntos_r3 = r1_3 + r2_3 + r4_3

		lista3.append(str(r1_3))
		lista3.append(str(r2_3))
		lista3.append(str(r4_3))
		lista3.append(str(puntos_r3))

		self.ui.resultado3.setText(str(puntos_r3))

		#Fila 4
		lista4 = []

		if not self.ui.lineEdit_1_4.text():
			r1_4 = 0
		else:
			r1_4 = int(self.ui.lineEdit_1_4.text())
		
		if not self.ui.lineEdit_2_4.text():
			r2_4 = 0
		else:
			r2_4 = int(self.ui.lineEdit_2_4.text())

		if not self.ui.lineEdit_3_4.text():
			r3_4 = 0
		else:
			r3_4 = int(self.ui.lineEdit_3_4.text()) 
		
		puntos_r4 = r1_4 + r2_4 + r3_4

		lista4.append(str(r1_4))
		lista4.append(str(r2_4))
		lista4.append(str(r3_4))
		lista4.append(str(puntos_r4))

		self.ui.resultado4.setText(str(puntos_r4))

		f = open('resultadosF.txt', 'w')

		for i in lista1:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista2:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista3:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista4:
			f.write( i + ' ')
		f.write('\n')	

		f.write("-------------" + '\n')

		f.close()

		# Primero y Segundo
		clasificacion = []
		clasificacion.append(int(lista1[3]))
		clasificacion.append(int(lista2[3]))
		clasificacion.append(int(lista3[3]))
		clasificacion.append(int(lista4[3]))

		#ordenamiento de mayor a menor
		for j in clasificacion:
			for i in range(0,3):
				if clasificacion[i] < clasificacion[i+1]:
					aux = clasificacion[i]
					clasificacion[i] = clasificacion[i+1]
					clasificacion[i+1] = aux

		if str(clasificacion[0]) == lista1[3]:
			primero = matriz[5]
			if str(clasificacion[1]) == lista2[3]:
				segundo = matriz[13]
			elif str(clasificacion[1]) == lista3[3]:
				segundo = matriz[21]
			else:
				segundo = matriz[29]

		elif str(clasificacion[0]) == lista2[3]:
			primero = matriz[13]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[5]
			elif str(clasificacion[1]) == lista3[3]:
				segundo = matriz[17]
			else:
				segundo = matriz[29]

		elif str(clasificacion[0]) == lista3[3]:
			primero = matriz[21]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[5]
			elif str(clasificacion[1]) == lista2[3]:
				segundo = matriz[13]
			else:
				segundo = matriz[29]

		else:
			primero = matriz[29]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[5]
			elif str(clasificacion[1]) == lista2[3]:
				segundo = matriz[13]
			else:
				segundo = matriz[21]

		print("primero", primero)
		print("segundo", segundo)
		primeros.insert(5,primero)
		segundos.insert(5,segundo)

	def resultadoG (self):
		self.ventana_2 = QtWidgets.QMainWindow()
		self.ui = Ui_ResultadoG()
		self.ui.setupUi(self.ventana_2)
		self.ventana_2.show() #Para ver

		b = banderas(matriz[6][2])
		self.ui.label_1.setStyleSheet(b.mostrar_bandera())
		self.ui.label_1_1.setText(str('  ' + matriz[6][1]+ '  ' + matriz[6][0]))

		b = banderas(matriz[14][2])
		self.ui.label_2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_2_2.setText(str('  ' + matriz[14][1]+ '  ' + matriz[14][0]))

		b = banderas(matriz[22][2])
		self.ui.label_3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_3_3.setText(str('  ' + matriz[22][1]+ '  ' + matriz[22][0]))

		b = banderas(matriz[30][2])
		self.ui.label_4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_4_4.setText(str('  ' + matriz[30][1]+ '  ' + matriz[30][0]))

		if path.exists("resultadosG.txt"):
			puntos = []
			fic = open("resultadosG.txt","r")
			lines = fic.readline()

			for j in range(0,4):
				puntos_jug = lines.split()
				for i in puntos_jug:
					puntos.append(i)
				lines = fic.readline()
	
			fic.close()

			self.ui.lineEdit_2_1.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_1.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_1.setText(str(puntos.pop(0)))
			self.ui.resultado1.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_2.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_2.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_2.setText(str(puntos.pop(0)))
			self.ui.resultado2.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_3.setText(str(puntos.pop(0)))
			self.ui.lineEdit_2_3.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_3.setText(str(puntos.pop(0)))
			self.ui.resultado3.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_4.setText(str(puntos.pop(0)))
			self.ui.lineEdit_2_4.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_4.setText(str(puntos.pop(0)))
			self.ui.resultado4.setText(str(puntos.pop(0)))


		self.ui.refrescar.clicked.connect(self.cuentaG)

	def cuentaG (self):

		#Fila 1
		lista1 = []

		if not self.ui.lineEdit_2_1.text():
			r2_1 = 0
		else:
			r2_1 = int(self.ui.lineEdit_2_1.text())
		
		if not self.ui.lineEdit_3_1.text():
			r3_1 = 0
		else:
			r3_1 = int(self.ui.lineEdit_3_1.text())

		if not self.ui.lineEdit_4_1.text():
			r4_1 = 0
		else:
			r4_1 = int(self.ui.lineEdit_4_1.text()) 
		
		puntos_r1 = r2_1 + r3_1 + r4_1
		lista1.append(str(r2_1))
		lista1.append(str(r3_1))
		lista1.append(str(r4_1))
		lista1.append(str(puntos_r1))

		self.ui.resultado1.setText(str(puntos_r1))

		#Fila 2
		lista2 = []

		if not self.ui.lineEdit_1_2.text():
			r1_2 = 0
		else:
			r1_2 = int(self.ui.lineEdit_1_2.text())
		
		if not self.ui.lineEdit_3_2.text():
			r3_2 = 0
		else:
			r3_2 = int(self.ui.lineEdit_3_2.text())

		if not self.ui.lineEdit_4_2.text():
			r4_2 = 0
		else:
			r4_2 = int(self.ui.lineEdit_4_2.text()) 
		
		puntos_r2 = r1_2 + r3_2 + r4_2

		lista2.append(str(r1_2))
		lista2.append(str(r3_2))
		lista2.append(str(r4_2))
		lista2.append(str(puntos_r2))

		self.ui.resultado2.setText(str(puntos_r2))

		#Fila 3
		lista3 = []

		if not self.ui.lineEdit_1_3.text():
			r1_3 = 0
		else:
			r1_3 = int(self.ui.lineEdit_1_3.text())
		
		if not self.ui.lineEdit_2_3.text():
			r2_3 = 0
		else:
			r2_3 = int(self.ui.lineEdit_2_3.text())

		if not self.ui.lineEdit_4_3.text():
			r4_3 = 0
		else:
			r4_3 = int(self.ui.lineEdit_4_3.text()) 
		
		puntos_r3 = r1_3 + r2_3 + r4_3

		lista3.append(str(r1_3))
		lista3.append(str(r2_3))
		lista3.append(str(r4_3))
		lista3.append(str(puntos_r3))

		self.ui.resultado3.setText(str(puntos_r3))

		#Fila 4
		lista4 = []

		if not self.ui.lineEdit_1_4.text():
			r1_4 = 0
		else:
			r1_4 = int(self.ui.lineEdit_1_4.text())
		
		if not self.ui.lineEdit_2_4.text():
			r2_4 = 0
		else:
			r2_4 = int(self.ui.lineEdit_2_4.text())

		if not self.ui.lineEdit_3_4.text():
			r3_4 = 0
		else:
			r3_4 = int(self.ui.lineEdit_3_4.text()) 
		
		puntos_r4 = r1_4 + r2_4 + r3_4

		lista4.append(str(r1_4))
		lista4.append(str(r2_4))
		lista4.append(str(r3_4))
		lista4.append(str(puntos_r4))

		self.ui.resultado4.setText(str(puntos_r4))

		f = open('resultadosG.txt', 'w')

		for i in lista1:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista2:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista3:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista4:
			f.write( i + ' ')
		f.write('\n')	

		f.write("-------------" + '\n')

		f.close()

		# Primero y Segundo
		clasificacion = []
		clasificacion.append(int(lista1[3]))
		clasificacion.append(int(lista2[3]))
		clasificacion.append(int(lista3[3]))
		clasificacion.append(int(lista4[3]))

		#ordenamiento de mayor a menor
		for j in clasificacion:
			for i in range(0,3):
				if clasificacion[i] < clasificacion[i+1]:
					aux = clasificacion[i]
					clasificacion[i] = clasificacion[i+1]
					clasificacion[i+1] = aux

		if str(clasificacion[0]) == lista1[3]:
			primero = matriz[6]
			if str(clasificacion[1]) == lista2[3]:
				segundo = matriz[14]
			elif str(clasificacion[1]) == lista3[3]:
				segundo = matriz[22]
			else:
				segundo = matriz[30]

		elif str(clasificacion[0]) == lista2[3]:
			primero = matriz[14]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[6]
			elif str(clasificacion[1]) == lista3[3]:
				segundo = matriz[17]
			else:
				segundo = matriz[30]

		elif str(clasificacion[0]) == lista3[3]:
			primero = matriz[22]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[6]
			elif str(clasificacion[1]) == lista2[3]:
				segundo = matriz[14]
			else:
				segundo = matriz[30]

		else:
			primero = matriz[30]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[6]
			elif str(clasificacion[1]) == lista2[3]:
				segundo = matriz[14]
			else:
				segundo = matriz[22]

		print("primero", primero)
		print("segundo", segundo)
		primeros.insert(6,primero)
		segundos.insert(6,segundo)

	def resultadoH (self):
		self.ventana_2 = QtWidgets.QMainWindow()
		self.ui = Ui_ResultadoH()
		self.ui.setupUi(self.ventana_2)
		self.ventana_2.show() #Para ver

		b = banderas(matriz[7][2])
		self.ui.label_1.setStyleSheet(b.mostrar_bandera())
		self.ui.label_1_1.setText(str('  ' + matriz[7][1]+ '  ' + matriz[7][0]))

		b = banderas(matriz[15][2])
		self.ui.label_2.setStyleSheet(b.mostrar_bandera())
		self.ui.label_2_2.setText(str('  ' + matriz[15][1]+ '  ' + matriz[15][0]))

		b = banderas(matriz[23][2])
		self.ui.label_3.setStyleSheet(b.mostrar_bandera())
		self.ui.label_3_3.setText(str('  ' + matriz[23][1]+ '  ' + matriz[23][0]))

		b = banderas(matriz[31][2])
		self.ui.label_4.setStyleSheet(b.mostrar_bandera())
		self.ui.label_4_4.setText(str('  ' + matriz[31][1]+ '  ' + matriz[31][0]))

		if path.exists("resultadosH.txt"):
			puntos = []
			fic = open("resultadosH.txt","r")
			lines = fic.readline()

			for j in range(0,4):
				puntos_jug = lines.split()
				for i in puntos_jug:
					puntos.append(i)
				lines = fic.readline()
	
			fic.close()

			self.ui.lineEdit_2_1.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_1.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_1.setText(str(puntos.pop(0)))
			self.ui.resultado1.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_2.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_2.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_2.setText(str(puntos.pop(0)))
			self.ui.resultado2.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_3.setText(str(puntos.pop(0)))
			self.ui.lineEdit_2_3.setText(str(puntos.pop(0)))
			self.ui.lineEdit_4_3.setText(str(puntos.pop(0)))
			self.ui.resultado3.setText(str(puntos.pop(0)))

			self.ui.lineEdit_1_4.setText(str(puntos.pop(0)))
			self.ui.lineEdit_2_4.setText(str(puntos.pop(0)))
			self.ui.lineEdit_3_4.setText(str(puntos.pop(0)))
			self.ui.resultado4.setText(str(puntos.pop(0)))

		self.ui.refrescar.clicked.connect(self.cuentaH)

	def cuentaH (self):

		#Fila 1
		lista1 = []

		if not self.ui.lineEdit_2_1.text():
			r2_1 = 0
		else:
			r2_1 = int(self.ui.lineEdit_2_1.text())
		
		if not self.ui.lineEdit_3_1.text():
			r3_1 = 0
		else:
			r3_1 = int(self.ui.lineEdit_3_1.text())

		if not self.ui.lineEdit_4_1.text():
			r4_1 = 0
		else:
			r4_1 = int(self.ui.lineEdit_4_1.text()) 
		
		puntos_r1 = r2_1 + r3_1 + r4_1
		lista1.append(str(r2_1))
		lista1.append(str(r3_1))
		lista1.append(str(r4_1))
		lista1.append(str(puntos_r1))

		self.ui.resultado1.setText(str(puntos_r1))

		#Fila 2
		lista2 = []

		if not self.ui.lineEdit_1_2.text():
			r1_2 = 0
		else:
			r1_2 = int(self.ui.lineEdit_1_2.text())
		
		if not self.ui.lineEdit_3_2.text():
			r3_2 = 0
		else:
			r3_2 = int(self.ui.lineEdit_3_2.text())

		if not self.ui.lineEdit_4_2.text():
			r4_2 = 0
		else:
			r4_2 = int(self.ui.lineEdit_4_2.text()) 
		
		puntos_r2 = r1_2 + r3_2 + r4_2

		lista2.append(str(r1_2))
		lista2.append(str(r3_2))
		lista2.append(str(r4_2))
		lista2.append(str(puntos_r2))

		self.ui.resultado2.setText(str(puntos_r2))

		#Fila 3
		lista3 = []

		if not self.ui.lineEdit_1_3.text():
			r1_3 = 0
		else:
			r1_3 = int(self.ui.lineEdit_1_3.text())
		
		if not self.ui.lineEdit_2_3.text():
			r2_3 = 0
		else:
			r2_3 = int(self.ui.lineEdit_2_3.text())

		if not self.ui.lineEdit_4_3.text():
			r4_3 = 0
		else:
			r4_3 = int(self.ui.lineEdit_4_3.text()) 
		
		puntos_r3 = r1_3 + r2_3 + r4_3

		lista3.append(str(r1_3))
		lista3.append(str(r2_3))
		lista3.append(str(r4_3))
		lista3.append(str(puntos_r3))

		self.ui.resultado3.setText(str(puntos_r3))

		#Fila 4
		lista4 = []

		if not self.ui.lineEdit_1_4.text():
			r1_4 = 0
		else:
			r1_4 = int(self.ui.lineEdit_1_4.text())
		
		if not self.ui.lineEdit_2_4.text():
			r2_4 = 0
		else:
			r2_4 = int(self.ui.lineEdit_2_4.text())

		if not self.ui.lineEdit_3_4.text():
			r3_4 = 0
		else:
			r3_4 = int(self.ui.lineEdit_3_4.text()) 
		
		puntos_r4 = r1_4 + r2_4 + r3_4

		lista4.append(str(r1_4))
		lista4.append(str(r2_4))
		lista4.append(str(r3_4))
		lista4.append(str(puntos_r4))

		self.ui.resultado4.setText(str(puntos_r4))

		f = open('resultadosH.txt', 'w')

		for i in lista1:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista2:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista3:
			f.write( i + ' ')
		f.write('\n')	
		for i in lista4:
			f.write( i + ' ')
		f.write('\n')	

		f.write("-------------" + '\n')

		f.close()

		# Primero y Segundo
		clasificacion = []
		clasificacion.append(int(lista1[3]))
		clasificacion.append(int(lista2[3]))
		clasificacion.append(int(lista3[3]))
		clasificacion.append(int(lista4[3]))

		#ordenamiento de mayor a menor
		for j in clasificacion:
			for i in range(0,3):
				if clasificacion[i] < clasificacion[i+1]:
					aux = clasificacion[i]
					clasificacion[i] = clasificacion[i+1]
					clasificacion[i+1] = aux

		if str(clasificacion[0]) == lista1[3]:
			primero = matriz[7]
			if str(clasificacion[1]) == lista2[3]:
				segundo = matriz[15]
			elif str(clasificacion[1]) == lista3[3]:
				segundo = matriz[23]
			else:
				segundo = matriz[31]

		elif str(clasificacion[0]) == lista2[3]:
			primero = matriz[15]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[7]
			elif str(clasificacion[1]) == lista3[3]:
				segundo = matriz[17]
			else:
				segundo = matriz[31]

		elif str(clasificacion[0]) == lista3[3]:
			primero = matriz[23]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[7]
			elif str(clasificacion[1]) == lista2[3]:
				segundo = matriz[15]
			else:
				segundo = matriz[31]

		else:
			primero = matriz[31]
			if str(clasificacion[1]) == lista1[3]:
				segundo = matriz[7]
			elif str(clasificacion[1]) == lista2[3]:
				segundo = matriz[15]
			else:
				segundo = matriz[23]

		print("primero", primero)
		print("segundo", segundo)
		primeros.insert(7,primero)
		segundos.insert(7,segundo)


	def cerrar (self):
		exit()


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = MyApp() 
	window.show()
	sys.exit(app.exec_())