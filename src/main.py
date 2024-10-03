import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Escolha qual funcionalidade deseja rodar
def yahoo_finance_analysis():
    # Baixar os dados da Apple e da Microsoft (ou outras empresas)
    apple = yf.download('AAPL', start='2023-01-01', end='2023-12-31')
    microsoft = yf.download('MSFT', start='2023-01-01', end='2023-12-31')

    # Exibir os primeiros dados
    print(apple.head())

    # Visualizar a comparação de preços ao longo do tempo
    plt.figure(figsize=(10,6))
    plt.plot(apple['Close'], label='Apple')
    plt.plot(microsoft['Close'], label='Microsoft')
    plt.title('Comparação de Preços das Ações (2023)')
    plt.xlabel('Data')
    plt.ylabel('Preço de Fechamento')
    plt.legend()
    plt.show()

    # Gráfico interativo com Plotly
    df = pd.DataFrame({
        'Date': apple.index,
        'Apple': apple['Close'],
        'Microsoft': microsoft['Close']
    })
    fig = px.line(df, x='Date', y=['Apple', 'Microsoft'], title='Comparação Interativa de Preços (Apple vs Microsoft)')
    fig.show()

    # Salvar os dados em CSV
    df.to_csv('apple_microsoft_prices_2023.csv', index=False)


def transport_analysis():
    print("A funcionalidade de transporte público está temporariamente indisponível.")
    # Código da função desativado até encontrarmos outro endpoint
    pass       


def web_scraping_jobs():
    # Buscar empregos de 'Product Owner' no Indeed
    url = 'https://www.indeed.com/jobs?q=product+owner&l=remote'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extrair títulos e links de vagas
    jobs = []
    for job_card in soup.find_all('div', class_='jobsearch-SerpJobCard'):
        title = job_card.find('h2', class_='title').text.strip()
        link = job_card.find('a')['href']
        jobs.append({'title': title, 'link': f"https://www.indeed.com{link}"})

    # Criar um DataFrame e visualizar as primeiras vagas
    df = pd.DataFrame(jobs)
    print(df.head())

    # Salvar em CSV
    df.to_csv('product_owner_jobs.csv', index=False)

# Escolha qual função rodar
print("Escolha qual análise deseja executar:")
print("1. Análise de Ações (Yahoo Finance)")
print("2. Análise de Transporte Público (London)")
print("3. Web Scraping de Empregos (Indeed)")
choice = input("Digite o número da opção: ")

if choice == "1":
    yahoo_finance_analysis()
elif choice == "2":
    transport_analysis()
elif choice == "3":
    web_scraping_jobs()
else:
    print("Escolha inválida.")