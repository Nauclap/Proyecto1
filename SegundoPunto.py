import numpy as np
#formato codigo
#0112222
#0 = año de ingreso
#11 = carrera
#2222 = numero de estudiante
uis = []
nombres = np.array(['Juan', 'David', 'Laura', 'Daniel', 'Hugo', 'Gabriela', 'Esteban', 'Monica', 'Luna'])
apellidos = np.array(['Rodriguez', 'Gomez', 'Vargas', 'Baron', 'Martinez', 'Naranjo', 'Pineda', 'Sanabria', 'Lopez'])
for i in range(1,6501):
    año = str(np.ceil(80+45*np.random.random()))
    carrera = str(int(np.ceil(9*np.random.random())))
    promedio = 2.8+ 2.2*np.random.random()    
    codigo = carrera+año[-4]+año[-3]+str(i)
    nombre_clave = np.ceil(8*np.random.random(2))
    nombre = nombres[int(nombre_clave[0])]+' '+apellidos[int(nombre_clave[1])]
    uis.append([codigo,nombre,promedio])


num_carrera = input('Ingrese una carrera del 1 al 9: ')
cantidad_1 = 0
cantitad_2 = 0
#for estudiante in uis:
   # print(f"Codigo: {estudiante[0]} Nombre:{estudiante[1]} Promedio: {estudiante[2]}")

print('---------------------------------------')
for estudiante in uis:    
    if estudiante[2]>= 4 and estudiante[0][0]==num_carrera:
        print(f"Codigo: {estudiante[0]} Nombre: {estudiante[1]} Promedio: {estudiante[2]}")
        cantidad_1 += 1
print(f'Hay {cantidad_1} estudiante(s) de la carrera {num_carrera} y promedio mayor o igual a 4')

print('---------------------------------------')

print('Estudiantes ingresados antes de 1990 y estan condicionales: ')
for estudiante in uis:
    if int(estudiante[0][1]+estudiante[0][2]) < 90 and int(estudiante[0][1]+estudiante[0][2])>26 and estudiante[2]>=2.8 and estudiante[2]<3.3:
        print(f"Codigo: {estudiante[0]} Nombre: {estudiante[1]} Promedio: {estudiante[2]}")
        cantitad_2 += 1
print(f'Hay {cantitad_2} estudiante(s) condicionales')   



