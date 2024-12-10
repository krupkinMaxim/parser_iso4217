from functions import save_to_excel

# Основной код 
if __name__ == "__main__": 
    url = 'https://en.wikipedia.org/wiki/ISO_4217'  # URL страницы 
    save_to_excel(df, 'currencies.xlsx')  # Сохраняем в Excel файл 