import mysql.connector
from tabulate import tabulate

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='db_g6'
)

#print('estas conectado a la base de datos')
print(f'estas conectado a a la base de datos : {connection.database}')


cursor = connection.cursor()
cursor.execute("select nombre,email from alumno")
resultado = cursor.fetchall()
#for registro in resultado:
#    print('**************')
#    print(f'Nombre : {registro[0]}')
#    print(f'Email : {registro[1]}')

#for nombre, email in resultado:
#    print('**************')
#    print(f'Nombre : {nombre}')
#    print(f'Email : {email}') 

columnas = ['id','dni','nombre','email','nota']

print(tabulate(resultado,headers=columnas,tablefmt='grid'))
    
connection.close() 