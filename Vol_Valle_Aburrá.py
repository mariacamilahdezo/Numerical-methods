#!/usr/bin/env python
# coding: utf-8

# # Primera tarea de Métodos Numéricos: ejercicio 5.

# Volumen del Valle de Aburrá: obtenido usando una malla de cuadriláteros, y aplicando Integración Gaussiana para obtener el área proyectada del valle.

# In[9]:


'''
Primera tarea de metodos numericos 2020-2
Realizada por: Maria Camila Hernández Ortiz, Sara Gómez Ramírez y Cristian Lopera Trujillo.

Requiere los archivos 'valle_aburra-quads.pts' y 'valle_aburra-quads.quad' como datos de entrada.
'''

#Se importan las librerías necesarias:
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import style
from matplotlib import cm

#Los datos de entradan se separan en elementos (quads) 
#y puntos coordenados (pts), cargando los archivos necesarios:

quads = np.loadtxt("valle_aburra-quads.quad", dtype=np.int)
pts = np.loadtxt("valle_aburra-quads.pts")/1000# Longitudes en km

#Para n=4 puntos se tienen matrices 4x4 para los valores de r y w que varían de acuerdo a la integración.
r=[math.sqrt((3-2*math.sqrt(6/5))/7),-(math.sqrt((3-2*math.sqrt(6/5))/7)),math.sqrt((3+2*math.sqrt(6/5))/7), -(math.sqrt((3+2*math.sqrt(6/5))/7))]
w=[(18+math.sqrt(30))/36,(18+math.sqrt(30))/36,(18-math.sqrt(30))/36,(18-math.sqrt(30))/36]

#Se crea un arreglo de unos y se inicializan las variables necesarias para la integración.
f=np.array([[1],[1],[1],[1]])
Puntomin=min(pts[:,2]) #Se halla el punto mínimo en la coordenada z (altura mínima).
VolTot=0
AreaTot=0  

#Se genera una lista en la que todos los elementos, dados ya en coordenadas, son almacenados usando un ciclo 'for' y luego
#se pasa a un arreglo denominado 'Cuadrilateros'.
Cuadrilateros=[]     
for m in range(len(quads)):    
    X0Y0=np.array([pts[quads[m,0],0], pts[quads[m,0],1], pts[quads[m,0],2]])
    X1Y1=np.array([pts[quads[m,1],0], pts[quads[m,1],1], pts[quads[m,1],2]])
    X2Y2=np.array([pts[quads[m,2],0], pts[quads[m,2],1], pts[quads[m,2],2]])
    X3Y3=np.array([pts[quads[m,3],0], pts[quads[m,3],1], pts[quads[m,3],2]])

    cuad=np.array([X0Y0, X1Y1, X2Y2, X3Y3])
    Cuadrilateros.append(cuad)
np.array(Cuadrilateros)


#Por medio de un ciclo 'for' que recorre los elementos y otros dos que corresponden a las iteraciones de integración (i,j),
#se halla el área de un cada cuadrilátero. Posteriormente se multiplica el área de cada elemento por una altura promedio
#entre las cuatro coordenadas en z.
#Finalmente, se suma el volumen de cada cuadrilátero, obteniendo además, el área proyectada.

for k in range(0,len(Cuadrilateros)):
    
    for i in range(0,len(r)):
        
        for j in range(0,len(r)):
            
            #Jacobiano para Integración Gaussiana.
            D=(0.25*np.array([[r[j]-1, -r[j]+1, r[j]+1, -r[j]-1],[r[i]-1, -r[i]-1, r[i]+1, -r[i]+1]]))
            J=np.linalg.det(np.dot(D,Cuadrilateros[k][:,:2]))
            
            #Interpoladores en dominio canónico, para la transformación.
            N0=(1/4)*(1-r[i])*(1-r[j])
            N1=(1/4)*(1+r[i])*(1-r[j])
            N2=(1/4)*(1+r[i])*(1+r[j])
            N3=(1/4)*(1-r[i])*(1+r[j])
            N=np.array([N0,N1,N2,N3])
            
            #Función a aplicar sumatoria (aproximación de integración).
            G=np.dot(N,Cuadrilateros[k][:,:2])
            Area=np.dot(N,f)*(J)*w[i]*w[j] #Cálculo del área de cada cuadrilátero.
            #Promedio de altura para cada elemento:
            Promedio=0.25*((Cuadrilateros[k][0,2])+(Cuadrilateros[k][1,2])+(Cuadrilateros[k][2,2])+(Cuadrilateros[k][3,2]))
            Alturamedia=Promedio-Puntomin
            Vol=Alturamedia*Area #Cálculo del volumen.
            AreaTot+=Area 
            VolTot+=Vol
    
#Se imprime el valor del volumen y el área 'proyectada' sobre un plano del Valle de Aburrá,
#luego de sumar todos los elementos (Cuadriláteros):

print("El área 'proyectada' del Valle de Aburrá es de: ",AreaTot," kilómetros al cuadrado.")    
print("El volumen del Valle de Aburrá es: ",VolTot," kilómetros al cubo.")   

'''
Gráfica del Valle de Aburrá
'''
style.use(('dark_background')) #Estilo de fondo

#Graficación en 3D
Valle = plt.figure()
ax = Axes3D(Valle)
ax.plot_trisurf(pts[:,0], pts[:,1], pts[:,2], cmap=cm.summer)
plt.title('Gráfica del Valle de Aburrá')

plt.grid(True,color='g')

#Definición de ejes (etiquetado y límites)
ax.set_xlim3d(0, 14.5)
ax.set_xlabel('$X$ $(Km)$')
ax.set_ylim3d(0, 30)
ax.set_ylabel('$Y$ $(Km)$')
ax.set_zlim3d(0.8, 4)
ax.set_zlabel('$Z$ $(Km)$')
ax.yaxis._axinfo['label']['space_factor'] = 3.0

#Fin del código.

