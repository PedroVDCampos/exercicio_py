# analise_cdi.py

import pandas as pd
import seaborn as sns
import requests, os, time, json
from datetime import datetime
from random import random
from sys import argv
import matplotlib.pyplot as plt

URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados'

def extrair_dados():
    print("🔍 Coletando taxa CDI...")
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

    print("✅ Dados salvos em taxa-cdi.csv")

def analisar_dados(nome_grafico="grafico_cdi"):
    df = pd.read_csv('taxa-cdi.csv')
    print("📊 Primeiras linhas dos dados:\n", df.head())

    grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
    _ = grafico.set_xticklabels(labels=df['hora'], rotation=90)
    grafico.get_figure().savefig(f"{nome_grafico}.png")

    print(f"📈 Gráfico salvo como {nome_grafico}.png")
    plt.show()

if __name__ == "__main__":
    nome = argv[1] if len(argv) > 1 else "grafico_cdi"
    extrair_dados()
    analisar_dados(nome)
