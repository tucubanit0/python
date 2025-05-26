import MySQLdb
# -*- coding: utf-8 -*-

# Datos de conexión a la base de datos
host = 'localhost'
puerto = 50167
usuario = 'root'
contraseña = '1234'
base_datos = 'prueba1'

try:
    # Establecer conexión a la base de datos
    conexion = MySQLdb.connect(host=host, port=puerto, user=usuario, passwd=contraseña, db=base_datos)
    
    # Crear un objeto cursor para ejecutar consultas
    cursor = conexion.cursor()
    
    # Sentencia SQL para crear la tabla
    sentencia = '''
    CREATE TABLE tabla_creada (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nombre VARCHAR(255),
        edad INT,
        estatura FLOAT
    )
    '''
    
    # Ejecutar la sentencia SQL
    cursor.execute(sentencia)
    
    # Confirmar los cambios en la base de datos
    conexion.commit()
    
    print("Tabla creada correctamente.")
    
    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()
    
except MySQLdb.Error as error:
    print("Error al conectarse a la base de datos:", error)