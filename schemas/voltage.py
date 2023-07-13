def voltageEntity(item) -> dict:
    return {
            'date': str(item['date']),
            'time': str(item['time']),
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
            'c_1': float(item['c_1'])
    }

def voltagesEntity(entity) -> list:
    return [voltageEntity(item) for item in entity]
