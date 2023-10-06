from fastapi import FastAPI
import mysql.connector
from mysql.connector import Error
from main import connection, disconnection

app = FastAPI()


connect = mysql.connector.connect(host="localhost", user="root", passwd="root", db="agendado")
cursor = connect.cursor()


@app.get("/update")
def update(idDoctor:int, Nombre:str, PrimerApe:str, SegundoApe:str, Celular:str, Especialidad:str, Correo:str, Cedula:str, HojaDoctor:str, Foto:str):
    connection()
    try:
        query = ("update doctor set Nombre=%s, PrimerApe=%s, SegundoApe=%s, Celular=%s, Especialidad=%s, Correo=%s, Cedula=%s,"
                 "HojaDoctor=%s, Foto=%s where idDoctor=%s;")
        val =(Nombre,PrimerApe,SegundoApe,Celular,Especialidad,Correo,Cedula,HojaDoctor,Foto,idDoctor)
        cursor.execute(query,val)
        connect.commit()
        #record = cursor.rowcount()
        #if record is not None:
        return {"Actualizado con exito"}
    except Error as e:
        return {"Error: ", e}
    disconnection()


@app.get("/updatePswrd")
def updatePswrd(idDoctor:int, Contrasena:str, ContrasenaNueva:str):
    connection()
    try:
        query = ("select * from doctor where idDoctor=%s  and Contrasena=%s;")
        val = (idDoctor, Contrasena)
        cursor.execute(query,val)
        record = cursor.fetchone()
        if record is not None:
            #return {record}
            #disconnection()
            #connection()
            try:
                query = ("update doctor set Contrasena=%s where idDoctor=%s;")
                val =(ContrasenaNueva,idDoctor)
                cursor.execute(query,val)
                connect.commit()
                #record = cursor.rowcount()
                #if record is not None:
                return {"Contraseña actualizada con exito"}
            except Error as e:
                return {"Error: ", e}
        disconnection()
    except Error as e:
        return {"Error: ", e}
    disconnection()
