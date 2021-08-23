#!/usr/bin/env python
# coding: utf-8

# # Primera tarea de Métodos Numéricos: ejercicio 4.

# Volumen de un caballo de ajedrez, calculado por medio de una malla de tetraedros, con unidades en mm$^3$.

# In[2]:


'''
Primera tarea de metodos numericos 2020-2
Realizada por: Maria Camila Hernández, Sara Gómez Ramírez y Cristian Lopera Trujillo.

Requiere el archivo 'knight.msh' como dato de entrada.
'''

#Se importan las librerías necesarias:
import numpy as np
import meshio #Librería meshio: necesaria para leer el archivo de mallado.

#La malla se "lee" desde un archivo .msh y se separa en elementos (tets) 
#y puntos coordenados (pts):
malla = meshio.read("knight.msh")
pts = malla.points
tets = malla.cells[0].data

#Se inicializa la variable "Volfinal" a la cual se va a añadir el volumen de cada tetraedro.
Volfinal=0

#Un ciclo "for" va hallando el volumen de cada tetraedro y lo va sumando 
#a la variable "Volfinal". (Recorre todos los elementos de tets).
for i in range(0,len(tets)):
    
    #Las coordenadas de cada vértice del tetraedro se definen (T1,T2,T3,T4).
    T1=np.array([pts[tets[i,0],0],pts[tets[i,0],1],pts[tets[i,0],2],1])
    T2=np.array([pts[tets[i,1],0],pts[tets[i,1],1],pts[tets[i,1],2],1])
    T3=np.array([pts[tets[i,2],0],pts[tets[i,2],1],pts[tets[i,2],2],1])
    T4=np.array([pts[tets[i,3],0],pts[tets[i,3],1],pts[tets[i,3],2],1])
    
    tetra=np.array([T1,T2,T3,T4])#Se genera la matriz de coordenadas del tetraedro.
    
    #El volumen se halla con el valor absoluto del determinante de la matriz anterior, multiplicada por 1/6.
    Vol=(1/6)*abs(np.linalg.det(tetra)) 
    
    Volfinal+= Vol #Se añade el volumen del tetraedro del ciclo, cada vez.

    
    
#Se imprime el valor del volumen del caballo de ajedrez, luego de sumar todos los elementos (tetraedros).
print('El volumen del caballo de ajedrez corresponde a:',Volfinal, 'milímetros cúbicos.')    

#Fin del código.

