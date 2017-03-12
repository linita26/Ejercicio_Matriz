import matriz
import random

def main():
    
    lista = ['MENU\n''1.Determinante', '2.Transpuesta', '3.Inversa', '4.MatrizValor', '5.Matriz_Elevada', '6.Matriz_Simetrica',
             '7.Matriz_Identidad', '8.Multiplicacion', '9.Resta', '10.Suma','11.Salir']

    for i in lista:
        print i
    opcion = int(input("Selecione La operacion que Desea Realizar "))
    if (opcion == 1):
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a=matrizA.llenarmatrizA()
         matrizA.imprimirmatriz()
         matrizA.matriz_det(a)

    if (opcion == 2):
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         matrizA.llenarmatrizA()
         matrizA.imprimirmatriz()
         matrizA.transpuesta()



    if (opcion == 4):
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         matrizA.llenarmatrizA()
         matrizA.imprimirmatriz()
         matrizA.matrizporvalor()

    if (opcion == 5):
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         matrizA.llenarmatrizA()
         matrizA.imprimirmatriz()
         matrizA.matriz_elevada()

    if (opcion == 6):
         matrizA = matriz.Matriz()
         matrizA.matrizSimetrica()

    if (opcion == 7):
         matrizA = matriz.Matriz()
         matrizA.matrizidentica()

    if (opcion == 8):
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a=matrizA.llenarmatrizA()
         matrizA.imprimirmatriz()
         columnasA = matrizA.getColumnas()
         filasA = matrizA.getFilas()

         matrizB = matriz.Matriz()
         matrizB.crearMatrizA()
         b = matrizB.llenarmatrizA()
         matrizB.imprimirmatrizC()

         columnasB = matrizB.getColumnas()
         filasB = matrizB.getFilas()
         matrizA.multiplicacionmatriz(filasA,columnasB,filasB,columnasA,a,b)

    if (opcion == 10):
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a = matrizA.llenarmatrizA()
         matrizA.imprimirmatriz()
         columnasA = matrizA.getColumnas()
         filasA = matrizA.getFilas()

         matrizB = matriz.Matriz()
         matrizB.crearMatrizA()
         b = matrizB.llenarmatrizA()
         matrizB.imprimirmatrizC()
         columnasB = matrizB.getColumnas()
         filasB = matrizB.getFilas()
         matrizA.sumamatriz(filasA, columnasB, filasB, columnasA, a, b)

    if (opcion == 9):
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a = matrizA.llenarmatrizA()
         matrizA.imprimirmatriz()
         columnasA = matrizA.getColumnas()
         filasA = matrizA.getFilas()

         matrizB = matriz.Matriz()
         matrizB.crearMatrizA()
         b = matrizB.llenarmatrizA()
         matrizB.imprimirmatrizC()

         columnasB = matrizB.getColumnas()
         filasB = matrizB.getFilas()
         matrizA.restamatriz(filasA, columnasB, filasB, columnasA, a, b)

    if (opcion == 11):
        print "Hasta Pronto"



if __name__ == '__main__':
    main()