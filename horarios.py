from fastapi import FastAPI
import mysql.connector
from mysql.connector import Error
from main import connection, disconnection

app = FastAPI()


connect = mysql.connector.connect(host="localhost", user="root", passwd="root", db="agendado")
cursor = connect.cursor()


@app.get("/addDates")
def addDates(idDoctor:int, fecha:str, hora:str,status:bool):
    connection()
    try:
        query = ("insert into horarios(idDoctor,fecha,hora,status) values(%s,%s,%s,%s);")
        val =(idDoctor, fecha, hora, status)
        cursor.execute(query,val)
        connect.commit()
        #record = cursor.rowcount()
        #if record is not None:
        return {"Insertado con exito"}
    except Error as e:
        return {"Error: ", e}


@app.get("/availableDates")
def availableDates(idDoctor:str):
    connection()
    try:
        query = ("select * from horarios where idDoctor="+idDoctor+" and status=true;")
        #print(query)
        #val = (idDoctor)
        cursor.execute(query)
        record = cursor.fetchall()
        #print(record)
        return record
    except Error as e:
        return {"Error: ", e}


@app.get("/deleteDates")
def deleteDates(idDoctor:int, fecha:str, hora:str):
    connection()
    try:
        query = ("select idhorarios from horarios where idDoctor=%s  and fecha=%s and hora =%s;")
        val = (idDoctor,fecha,hora)
        cursor.execute(query, val)
        record = cursor.fetchone()
        if record is not None:
            #return {record}
            # disconnection()
            # connection()
            try:
                query = ("delete from horarios where idhorarios=%s;")
                val = (record)
                cursor.execute(query, val)
                connect.commit()
                # record = cursor.rowcount()
                # if record is not None:
                return {"Eliminado con exito"}
            except Error as e:
                disconnection()
                return {"Error: ", e}
    except Error as e:
        disconnection()
        return {"Error: ", e}


