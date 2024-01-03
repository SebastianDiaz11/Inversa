"""
5. Definir una funcion inversa() que calcule la inversion de una cadena. 
Por ejemplo la cadena "estoy probando" deberia devolver la cadena "odnaborp yotse".
"""

def inversa(cadena):
    #Le resto 1 por que empieza contando desde 0
    longitud = -(len(cadena)-1) 
    nueva_cadena = str ()
    #Hago el conteo de atras para delante
    for n in range(longitud,1):
        #Vuelvo positivo al numero
        n = abs(n)
        nueva_cadena += cadena[n]
    print(nueva_cadena)

inversa('pepito')
inversa('54321')