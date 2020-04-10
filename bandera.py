class banderas:

	def __init__(self,bandera):
	 	self.band = bandera


	def mostrar_bandera(self):
		if self.band == 'VZLA':
			img = "border-image: url(:/vzla/vzla.jpeg);"
			return(img)

		elif self.band == 'TRU':
			img = "border-image: url(:/tru/tru.png);"
			return(img)

		elif self.band == 'lichess':
			img = "border-image: url(:/lichess/lichess.jpeg);"
			return(img)

		elif self.band == 'MER':
			img = "border-image: url(:/mer/mer.png);"
			return(img)

		elif self.band == 'APU':
			img = "border-image: url(:/apure/apure.png);"
			return(img)

		elif self.band == 'CAR':
			img = "border-image: url(:/car/carabobo.png);"
			return(img)


			