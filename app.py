from fastapi import FastAPI
import json
from db import conn
from schemas.voltage import voltageEntity, voltagesEntity
from models.voltage import Voltage
from datetime import datetime
import pytz

app=FastAPI(
                title="LoggerMega",
                version="1.0",
                contact={
                            "name": "v1c4r10us",
                            "email": "v1c4r10us.29@gmail.com",
                },
                license_info={
                            "name": "Apache 2.0",
                            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
                }
            )

@app.get('/', tags=['Welcome'])
def welcome():
    return {'version': 'v1.0', 
            'published':'2023',
            'contributors': 'Edgard Huanca & Michaell Huanca',
            'github':'https://github.com/v1c4r10us/logger-mega',
            'documentation':'https://logger-mega.vercel.app/docs'}

@app.post('/voltage', response_model=Voltage, tags=['Voltage'])
def save_new(voltage: Voltage):
    new_voltage=dict(voltage)
    tzInfo=pytz.timezone('America/Lima')
    now=datetime.now(tz=tzInfo)
    date=now.strftime('%d-%m-%Y')
    time=now.strftime('%H:%M:%S')
    new_voltage['date']=date
    new_voltage['time']=time
    id=conn.Logger.Voltage.insert_one(new_voltage).inserted_id
    voltage=conn.Logger.Voltage.find_one({"_id":id})
    return voltageEntity(voltage)

@app.get('/voltages',response_model=list[Voltage], tags=['Get-Voltages'])
def get_All():
    return voltagesEntity(conn.Logger.Voltage.find())
