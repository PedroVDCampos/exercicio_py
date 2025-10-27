import pandas as pd
import seaborn as sns
import requests, os, time, json
from datetime import datetime
from random import random
import matplotlib.pyplot as plt

URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados'

# Coleta os dados do Banco Central
response = requests.get(URL)
dado = json.loads(response.text)[-1]['valor']

# Gera 5 registros simulando coletas
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

# Lê o CSV com o Pandas
df = pd.read_csv('taxa-cdi.csv')
print(df.head())

# Cria o gráfico com Seaborn
grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
_ = grafico.set_xticklabels(labels=df['hora'], rotation=90)
grafico.get_figure().savefig("grafico_cdi.png")

print("📈 Gráfico gerado: grafico_cdi.png")
plt.show()
