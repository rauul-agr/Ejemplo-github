# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	datos = [str() for ind0 in range(200)]
	print("Ingrese la cantidad de datos (de 2 a 200):")
	n = float(input())
	for i in range(1,n+1):
		print("Ingrese el dato ",i,":")
		datos[i] = input()
	if datos[1]>datos[2]:
		may1 = datos[1]
		may2 = datos[2]
	else:
		may1 = datos[2]
		may2 = datos[1]
	for i in range(3,n+1):
		if datos[i]>may1:
			may2 = may1
			may1 = datos[i]
		else:
			if datos[i]>may2:
				may2 = datos[i]
	print("El mayor es: ",may1)
	print("El segundo mayor es: ",may2)

