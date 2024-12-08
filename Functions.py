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
        