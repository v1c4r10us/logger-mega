from fastapi import FastAPI
import json
from db import conn
from datetime import datetime

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

@app.get('/')
def welcome():
    return {'version': 'v1.0', 
            'published':'2023',
            'contributors': 'Edgard Huanca & Michaell Huanca',
            'github':'https://github.com/v1c4r10us/logger-mega',
            'documentation':''}

@app.post('/save/{voltage}')
def save(voltage: float):
    now=datetime.now()
    now=now.strftime('%d-%m-%Y %H:%M:%S')
    new_voltage={now:voltage}
    db=conn['logger']
    collection=db['voltage']
    collection.insert_one(new_voltage)
    return {'server_says':'A new voltage added successfully!'}
