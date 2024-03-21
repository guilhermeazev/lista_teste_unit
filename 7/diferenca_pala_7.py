from datetime import datetime, timedelta

def diferenca_entre_datas(data1, data2):

    data1 = datetime.strptime(data1, '%Y-%m-%d %H:%M:%S')
    data2 = datetime.strptime(data2, '%Y-%m-%d %H:%M:%S')

    diferenca = data2 - data1

    return {
        'dias': diferenca.days,
        'meses': diferenca.days // 30,  # Aproximação de meses, considerando 30 dias em um mês
        'anos': diferenca.days // 365,  # Aproximação de anos, considerando 365 dias em um ano
        'horas': diferenca.total_seconds() // 3600,
        'minutos': diferenca.total_seconds() // 60
    }