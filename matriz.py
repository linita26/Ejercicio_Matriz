#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import random

class Matriz(object):

    def __init__(self, filas=None, columnas=None):


        if filas:
            self.filas=filas
        else:
            self.filas=int(raw_input("Ingrese Cantidad de Filas "))
        if columnas:
            self.columnas= columnas
        else:
            self.columnas = int(raw_input("ingrese Cantidad de Columnas "))

    def crearMatrizA(self):
        self.matriz=[]
        for f in range(self.filas):
            self.matriz.append([0]*self.columnas)

    def llenarmatrizA(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = random.randint(0, 10)

                    #int(raw_input("ingrese %d, %d: " % (f, c)))
        return self.matriz

    def imprimirmatriz(self):
        cadena = ""
        for i in range(self.filas):
            for j in range(self.columnas):
                if j == self.columnas - 1:
                    cadena = cadena + str(self.matriz[i][j]) + "\n"
                else:
                    cadena = cadena + str(self.matriz[i][j]) + "  "


        print "Matriz A "+'\n' + cadena

    def imprimirmatrizC(self):
        cadena = ""
        for i in range(self.filas):
            for j in range(self.columnas):
                if j == self.columnas - 1:
                    cadena = cadena + str(self.matriz[i][j]) + "\n"
                else:
                    cadena = cadena + str(self.matriz[i][j]) + "  "


        print "Matriz B "+'\n' + cadena

    def imprimirmatrizB(self,matrizB):
        cadena = ""
        for i in range(self.filas):
            for j in range(self.columnas):
                if j == self.columnas - 1:
                    cadena = cadena + str(matrizB[i][j]) + "\n"
                else:
                    cadena = cadena + str(matrizB[i][j]) + "  "
        return cadena

    def matriz_det(self,b):

        if (self.filas != self.columnas):
            print "La matriz Debe ser Cuadrada "
            return True
        elif self.filas==2:
                a=1
                b=1
                for f in range(self.filas):
                    for c in range(self.columnas):
                        if f==c:
                            a*=self.matriz[f][c]
                        else:
                            b*=self.matriz[f][c]
                det=a-b

                print "El determinante es "+str(det)
                return det
        else:
                m = self.matrizcopy(b)
                n = len(m)
                det = 1
                for i in range(n):
                    j = self.primeroNoNulo(m,i)
                    if j == n:
                        return 0
                    if i != j:
                        det = -1 * det
                        self.intercambiaFilas(m, i, j)
                    det = det * m[i][i]
                    self.multiplicaFila(m, i, 1. / m[i][i])
                    for k in range(i + 1, n):
                        self.combinacion(m, i, k, -m[k][i])

                print "El determinante es " + str(det)
                return det

    def matrizcopy(self, matriz):
        self.result = []
        for f in matriz:
            self.result.append(f[:])
        return self.result

    def primeroNoNulo(self,m,i):
        result = i
        while result < len(m) and m[result][i] == 0:
            result = result + 1
        return result

    def intercambiaFilas(self, m,i,j):
        m[i], m[j] = m[j], m[i]

    def multiplicaFila(self, m, f, e):

        n = len(m)
        for c in range(n):
            m[f][c] = m[f][c] * e



    def combinacion(self, m,i,j,e):
        n = len(m)
        for c in range(n):
            m[j][c] = m[j][c] + e * m[i][c]

    def transpuesta(self):

        self.matrizB = []
        for f in range(self.columnas):
            self.matrizB.append([0] * self.filas)

        for i in range(self.filas):
            for j in range(self.columnas):
                self.matrizB[j][i] = self.matriz[i][j]

        a=self.imprimirmatrizB(self.matrizB)
        print a
        return self.matrizB

    def matrizporvalor(self):
            self.matrizB = []
            for f in range(self.columnas):
                self.matrizB.append([0] * self.filas)
            a = int(raw_input("ingrese valor a Multiplicar "))
            for i in range(self.filas):
                for j in range(self.columnas):
                    self.matrizB[i][j]= self.matriz[i][j]*a
            b = self.imprimirmatrizB(self.matrizB)
            print b

    def matriz_elevada(self):

        self.matrizC = []
        for i in range(self.filas):
            self.matrizC.append([0] * self.columnas)
        a = int(raw_input("ingrese numero para Elevar la Matriz "))

        if a==2:
            for i in range(self.filas):
                for j in range(self.columnas):
                    for k in range(self.columnas):
                        self.matrizC[i][j] += self.matriz[i][k] * self.matriz[k][j]

            b = self.imprimirmatrizB(self.matrizC)
            print b
        if a==3:
            self.matrizD = []
            for i in range(self.filas):
                self.matrizD.append([0] * self.columnas)

            for i in range(self.filas):
                for j in range(self.columnas):
                    for k in range(self.columnas):
                        self.matrizC[i][j] += self.matriz[i][k] * self.matriz[k][j]

            for i in range(self.filas):
                for j in range(self.columnas):
                    for k in range(self.columnas):
                        self.matrizD[i][j] += self.matrizC[i][k] * self.matriz[k][j]

            b = self.imprimirmatrizB(self.matrizD)
            print  b

    def matrizSimetrica(self):

        self.matriz=[]

        for f in range(self.filas):
            auxiliar = []
            for c in range(self.columnas):
                elemento = random.randint(0,10)


                auxiliar.append(elemento)
            self.matriz.append(auxiliar)

        a =self.imprimirmatrizB(self.matriz)
        print "Matriz "+ '\n' + a

        matriz_T= self.transpuesta()

        if matriz_T == self.matriz:
            print "es simetrica"
        else:
            print "no es simetrica"


    def matrizidentica(self):

        self.matriz = []

        for f in range(self.filas):
            auxiliar = []
            for c in range(self.columnas):
                elemento = random.randint(0,10)

                auxiliar.append(elemento)
            self.matriz.append(auxiliar)

        a = self.imprimirmatrizB(self.matriz)
        print "Matriz  " + '\n' + a

        if (self.filas != self.columnas):
            print "No se puede hallar la matriz"

        else:

            self.matrizI=[]
            for i in range(self.filas):
                self.matrizI.append([0] * self.columnas)

            for f in range(self.filas):
               for c in range(self.columnas):
                    if f == c:
                        self.matrizI[f][c]=1
                    else:
                        self.matrizI[f][c]= 0

            b = self.imprimirmatrizB(self.matrizI)
            print "Matriz Identidad " + '\n' + b

    def multiplicacionmatriz(self, filasA, columnasB, filasB,columnasA,matrizA,matrizB):

        if (filasB != columnasA):
            print "No se puede hacer la operacion"
        else:
            self.matrizC = []
            for i in range(filasA):
                self.matrizC.append([0] * columnasB)

            for i in range(filasA):
                for j in range(columnasB):
                    for k in range(filasB):
                        self.matrizC[i][j] += matrizA[i][k] * matrizB[k][j]

            b = self.imprimirmatrizB(self.matrizC)
            print  b

    def sumamatriz(self, filasA, columnasB, filasB,columnasA,matrizA,matrizB):

        if (filasA == filasB and columnasA == columnasB):

            self.matrizC = []
            for i in range(filasA):
                self.matrizC.append([0] * columnasB)

            for i in range(filasA):
                for j in range(columnasA):
                        self.matrizC[i][j] = matrizA[i][j] + matrizB[i][j]

            b = self.imprimirmatrizB(self.matrizC)
            print b

        else:
            print "no se puede realizar la operacion"

    def restamatriz(self, filasA, columnasB, filasB,columnasA,matrizA,matrizB):

        if (filasA == filasB and columnasA == columnasB):

            self.matrizC = []
            for i in range(filasA):
                self.matrizC.append([0] * columnasB)

            for i in range(filasA):
                for j in range(columnasA):
                        self.matrizC[i][j] = matrizA[i][j] - matrizB[i][j]

            b = self.imprimirmatrizB(self.matrizC)
            print b

        else:
            print "no se puede Hacer la operacion"



    def getFilas(self):
        return self.filas

    def getColumnas(self):
        return self.columnas

