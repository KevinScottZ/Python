import pandas as pd
from datetime import date, timedelta

# Definindo os feriados nacionais e estaduais de São Paulo em 2024
feriados_sp_2024 = [
    date(2024, 1, 1),   # Ano Novo
    date(2024, 2, 24),  # Carnaval
    date(2024, 2, 25),  # Carnaval
    date(2024, 4, 21),  # Tiradentes
    date(2024, 5, 1),   # Dia do Trabalho
    date(2024, 6, 20),  # Corpus Christi
    date(2024, 9, 7),   # Independência do Brasil
    date(2024, 10, 12), # Nossa Senhora Aparecida
    date(2024, 11, 2),  # Finados
    date(2024, 11, 15), # Proclamação da República
    date(2024, 12, 25)  # Natal
]

# Função para verificar se uma data é feriado em São Paulo
def is_feriado_sp(date):
    return date.weekday() >= 5 or date in feriados_sp_2024

# Gerar lista de dias úteis em 2024
def dias_uteis_sp(start_date, end_date):
    dias_uteis = []
    current_date = start_date
    while current_date <= end_date:
        if not is_feriado_sp(current_date):
            dias_uteis.append(current_date)
        current_date += timedelta(days=1)
    return dias_uteis

# Definindo o intervalo de datas para 2024
start_date = date(2024, 1, 1)
end_date = date(2024, 12, 31)

# Obtendo os dias úteis de São Paulo em 2024
dias_uteis = dias_uteis_sp(start_date, end_date)

# Criando um DataFrame pandas com as datas úteis
df = pd.DataFrame({'data': dias_uteis})

# Salvando o DataFrame em um arquivo CSV
csv_file = 'dias_uteis_sp_2024.csv'
df.to_csv(csv_file, index=False)

print(f'Arquivo CSV criado com sucesso: {csv_file}')
