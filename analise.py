import pandas as pd
import cybor as cb
import requests
from datetime import datetime
from random import random
import time, os, json

URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados'

response = requests.get(URL)
dado = json.loads(response.text)[-1]['valor']

for _ in range(5): 
    data = datetime.now().strftime('%Y/%m/%d')
    hora = datetime.now().strftime('%H:%M:%S')
    cdi = float(dado) + (random() - 0.5)

    if not os.path.exists('taxa-cdi.csv'):
        with open('taxa-cdi.csv', 'w', encoding='utf8') as f:
            f.write('data,hora,taxa\n')

    with open('taxa-cdi.csv', 'a', encoding='utf8') as f:
        f.write(f'{data},{hora},{cdi}\n')

    time.sleep(1)

print("✅ Dados coletados e salvos em taxa-cdi.csv")

df = pd.read_csv('taxa-cdi.csv')
print(df.head())

relatorio = cb.analyze(df)
print(relatorio.summary())

relatorio.to_html("relatorio_cdi.html")
print("📊 Relatório gerado: relatorio_cdi.html")
