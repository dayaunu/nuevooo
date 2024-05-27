#DATAFRAME
#creacion de dataframe a partir de un diccionario
#primera forma de crear
import pandas as pd

datos = {'nombre':['María', 'Luis', 'Carmen', 'Antonio'],
'edad':[18, 22, 20, 21],
'grado':['Economía', 'Medicina', 'Arquitectura', 'Economía'],
'correo':['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']
    }
#forma de crear un dataframe
df = pd.DataFrame(datos)
print(df)

#creacion de un dataframe a partir de una lista de listas
df = pd.DataFrame([["María", 18], ["Luis", 22], ["Carmen", 20], ["Antonio", 21]], 
                  columns=["nombre", "edad"])

print(df)

#creacion de un dataframe a partir de una lista de diccionarios
df = pd.DataFrame([{"nombre": "María", "edad": 18}, {"nombre": "Luis",
"edad": 22}, {"nombre": "Carmen", "edad": 20}, {"nombre": "Antonio", "edad": 21}])

print(df)

#creacion de un dataframe a partir de un array
df = pd.DataFrame([[2,3,4],[5,22,1]], columns=["a", "b", "c"])
print(df)

#numeros aleatorios
import numpy as np
df = pd.DataFrame(np.random.randn(4, 3), columns=["a", "b", "c"])
print(df)