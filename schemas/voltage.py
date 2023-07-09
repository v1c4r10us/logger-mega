def voltageEntity(item) -> dict:
    return {
            'date': item['date'],
            'time': item['time'],
            's_1': float(item['s_1']),
            's_2': float(item['s_2']),
            's_3': float(item['s_3']),
            's_4': float(item['s_4']),
            's_5': float(item['s_5'])
    }
