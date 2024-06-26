import random
def generarDatos():
    datos = []
    for i in range(5000):
        dato={}
        id=random.randint(1,10000)
        referencia=random.choice(["ACH01","ACH22","ACH43"])
        marca=random.choice(["soni","rico","kalley"])
        capacidad=random.randint(100,2000)
        ciudad=random.choice(["Medellin","Bello","Sabaneta","Itagui","Bogota"])
        responsable=random.choice(["Juan jose ospina","Diego ospina","Sonia gil","tattiana ossa","Carlos ortiz"])

        dato=[id,referencia,marca, capacidad,ciudad,responsable]
        datos.append(dato)
    return datos

print(generarDatos())

