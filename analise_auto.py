import pandas as pd
import cybor as cb
import requests, os, time, json
from datetime import datetime
from random import random
from sys import argv

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

def analisar_dados(nome_relatorio="relatorio_cdi"):
    df = pd.read_csv('taxa-cdi.csv')
    print("📈 Primeiras linhas:\n", df.head())

    relatorio = cb.analyze(df)
    print("\n🧠 Resumo da análise:")
    print(relatorio.summary())

    relatorio.to_html(f"{nome_relatorio}.html")
    print(f"\n✅ Relatório salvo como {nome_relatorio}.html")

if __name__ == "__main__":
    nome = argv[1] if len(argv) > 1 else "relatorio_cdi"
    extrair_dados()
    analisar_dados(nome)
