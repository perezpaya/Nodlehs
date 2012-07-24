import math, time

#Variables

#velocidad (50 km/h, 70 km/h, 90 km/h, 110 km/h y 120 km/h)
#conversion a m/s
v1 = float(50*1000/3600)
v2 = float(70*1000/3600)
v3 = float(90*1000/3600)
v4 = float(110*1000/3600)
v5 = float(120*1000/3600)

#aceleraciones
a1 = float(10)
a2 = float(5)
#Formulas
	#Cinematica
		# MRUA: xf = xi+vi*t+1/2*a*t^2
		# Caida Libre: xf = 1/2*a*t^2
	# Distancia seguridadd=v*t+v^2*(a1-a2)/2*a1*a2
	#
#Inicializacion de la variables

loopNumber = int(1)

print("____________________________________________")
print("Nodlehs dice: Bienvenido usuario____________")
print("____________________________________________")
print("Nodlehs dice: Trabajo en unidades del sistema internacional, tenlo encuenta")
print("Nodlehs dice: Tengo problemas al poner las tildes, ya que no soy nativo, la omitire querido usuario")
print("Nodlehs dice: Comenzemos!")
print("____________________________________________")

time.sleep(3)

while (loopNumber <= 5):
	
	xf = float(input("Nodlehs dice: Cual es el espacio recorrido? (En metros) "))
	g = 9.81
	div = 9.81*0.5
	t = math.sqrt(xf/div)
	
	print("El tiempo de reaccion es de %s s" % t)
	
	time.sleep(5)
	
	print("Ahora calcularemos la distancia de seguridad")
	
	commonCalc = float(a1-a2)
	commonCalc = commonCalc/(2*a1*a2)

	d1 = float(v1*t+v1*v1*commonCalc)
	d2 = float(v2*t+v2*v2*commonCalc)
	d3 = float(v3*t+v3*v3*commonCalc)
	d4 = float(v4*t+v4*v4*commonCalc)
	d5 = float(v5*t+v5*v5*commonCalc)

	print("La distancia de seguridad a %s m/s es de %s m" %(v1, d1))
	print("La distancia de seguridad a %s m/s es de %s m" %(v2, d2))
	print("La distancia de seguridad a %s m/s es de %s m" %(v3, d3))
	print("La distancia de seguridad a %s m/s es de %s m" %(v4, d4))
	print("La distancia de seguridad a %s m/s es de %s m" %(v5, d5))
	loopNumber = loopNumber+1
print("El programa finalizo con exito")
