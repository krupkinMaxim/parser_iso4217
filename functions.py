import requests 
from bs4 import BeautifulSoup 
import pandas as pd

def save_to_excel(df, file_name): 
    """Функция для сохранения DataFrame в Excel файл.""" 
    df.to_excel(file_name, index=False, engine='openpyxl') 
    print(f"Таблица успешно сохранена в файл: {file_name}")
