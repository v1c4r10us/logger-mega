from datetime import datetime
import pytz

def voltageEntity(item) -> dict:
    tzInfo = pytz.timezone('America/Lima')
    now=datetime.now(tz=tzInfo)
    date=now.strftime('%d-%m-%Y')
    time=now.strftime('%H:%M:%S')
    return {
            'date': str(date),
            'time': str(time),
            's_1': float(item['s_1']),
            's_2': float(item['s_2']),
            's_3': float(item['s_3']),
            's_4': float(item['s_4']),
            's_5': float(item['s_5']),
            's_6': float(item['s_6']),
            's_7': float(item['s_7']),
            's_8': float(item['s_8']),
            's_9': float(item['s_9']),
            's_10': float(item['s_10']),
            's_11': float(item['s_11']),
            's_12': float(item['s_12']),
            's_13': float(item['s_13']),
            's_14': float(item['s_14']),
            's_15': float(item['s_15']),
            's_16': float(item['s_16']),
            's_17': float(item['s_17']),
            's_18': float(item['s_18']),
            's_19': float(item['s_19'])
    }

def voltagesEntity(entity) -> list:
    return [voltageEntity(item) for item in entity]
