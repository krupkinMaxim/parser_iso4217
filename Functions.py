import requests 
from bs4 import BeautifulSoup 
import pandas as pd 

def get_currency_data(url):
    """Функция для получения данных о валютах с веб-страницы."""
    # Запрос к странице
    response = requests.get(url)
    response.raise_for_status()  # Проверка на успешный запрос

    # Парсинг страницы
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим таблицу с кодами валют
    table = soup.find('table', {'class': 'wikitable'})
    
    # Списки для хранения данных
    currencies = []
    countries = []
    codes = []
    symbols = []
    
    # Проходим по строкам таблицы (пропускаем первую строку с заголовками)
    for row in table.find_all('tr')[1:]:
        columns = row.find_all('td')
        
        if len(columns) >= 4:  # Проверяем, что строка содержит достаточное количество данных
            country = columns[0].get_text(strip=True)
            code = columns[1].get_text(strip=True)
            symbol = columns[2].get_text(strip=True)
            currency = columns[3].get_text(strip=True)

            countries.append(country)
            codes.append(code)
            symbols.append(symbol)
            currencies.append(currency)
              # Создаем DataFrame
    data = {
        'Country': countries,
        'Currency': currencies,
        'Currency Code': codes,
        'Symbol': symbols
    }

    return pd.DataFrame(data)


def save_to_excel(df, file_name): 
    """Функция для сохранения DataFrame в Excel файл.""" 
    df.to_excel(file_name, index=False, engine='openpyxl') 
    print(f"Таблица успешно сохранена в файл: {file_name}")
