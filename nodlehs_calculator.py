import math, time;

print("____________________________________________");
print("Nodlehs dice: Bienvenido usuario____________");
print("____________________________________________");
print("Nodlehs dice: Trabajo en unidades del sistema internacional, tenlo encuenta");
print("Nodlehs dice: Tengo problemas al poner las tildes, ya que no soy nativo, la omitire querido usuario");
print("Nodlehs dice: Comenzemos!");
print("____________________________________________");
time.sleep(4);
main = "no";
loop = "si";

#xf = xi+vi*t+1/2*a*t^2
#xf = 1/2*a*t^2
while(main =="no"):
	while (loop == "SI" or loop == "si" ):
		xf = float(raw_input("Nodlehs dice: Cual es el espacio recorrido? (En metros) "));
		t = 0.5*9.8/xf;
		t = math.sqrt(t);
		print("El tiempo de reaccion es de ",t," segundos");
		ask = raw_input(" Desea volver a realizar este calculo? ");
		if(ask == "si"):
			print("Nodlehs dice: Reiniciando el bucle");
		else:
			loop = "no";
	print("Ahora calcularemos la distancia de seguridad");

	main = raw_input("Desea finalizar el programa? ");
print("El programa finalizo con exito");