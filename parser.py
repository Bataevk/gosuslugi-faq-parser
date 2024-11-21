import requests
import os
import re
from bs4 import BeautifulSoup

# Базовый URL сайта госуслуг
# BASE_URL = "https://www.gosuslugi.ru"

# print(requests.get("https://www.gosuslugi.ru/api/cms/v2/faq/categories/about_gosuslugi/general").json())

url = input('Введите ссылку на страницу: ')
path = url.split('faq/')[-1].strip('/')

# URL API для получения данных
API_URL = "https://www.gosuslugi.ru/api/cms/v2/faq/categories/" + path


# Удаление подкатегории
API_URL = "/".join(API_URL.split('/subcategory/'))

print("Request to API URL: " + API_URL)

# Функция для преобразования HTML в текст с форматированием ссылок
def clean_html_with_links(raw_html):
    soup = BeautifulSoup(raw_html, "html.parser")
    
    # Обрабатываем все ссылки
    for a_tag in soup.find_all("a"):
        text = a_tag.get_text(strip=True)  # Текст ссылки
        href = a_tag.get("href")           # URL ссылки
        if href:
            markdown_link = f"[{text}]({href})"
            a_tag.replace_with(markdown_link)
    
    # Возвращаем текст с учётом преобразованных ссылок
    return soup.get_text(separator="\n").strip()

# Преобразование заголовка в допустимое имя файла
def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "_", filename)



def extract_data(data, dir = 'articles'):

    articles = data.get("faqs", [])
    
    # Создаем папку для статей
    if not os.path.exists(dir):
        os.makedirs(dir)
    
    # Обрабатываем каждую статью
    for article in articles:
        title = article.get("title", "Без названия")
        raw_answer = article.get("answer", "")
        
        # Очищаем текст ответа от HTML и обрабатываем ссылки
        cleaned_answer = f'{title}\n\n{clean_html_with_links(raw_answer)}'
        
        # Преобразуем заголовок в имя файла
        filename = sanitize_filename(title) + ".txt"
        
        # Сохраняем статью в файл
        filepath = os.path.join(dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(cleaned_answer)
        
        print(f"Сохранено: {filepath}")


# Главная функция
def main():
    # Отправляем GET-запрос к API
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        data = response.json()

        title = data.get('title','articles')

        for child in data.get('children',[]):
            extract_data(child, title)
        else:
            extract_data(data, title)


    else:
        print(f"Ошибка запроса к API: {response.status_code}")

if __name__ == "__main__":
    main()
