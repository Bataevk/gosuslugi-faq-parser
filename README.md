# Parser for Gosuslugi FAQ

A simple Python script to parse FAQ data from the Gosuslugi website and save it as text files.

## Содержание

- [Требования](#требования)
- [Установка](#установка)
- [Использование](#использование)
- [Пример использования](#пример-использования)

## Требования

1. **Python 3.x**
2. **Библиотеки:**
   - `requests`
   - `beautifulsoup4`

## Установка

1. **Установите необходимые библиотеки:**
   ```sh
   pip install requests beautifulsoup4
   ```

## Использование

1. **Запустите скрипт с помощью команды:**
   ```sh
   python parser.py
   ```

2. **Введите ссылку на страницу FAQ с сайта Gosuslugi, когда будет предложено.**

## Пример использования

1. **Запуск скрипта:**
   ```sh
   python parser.py
   ```

2. **Ввод ссылки:**
   ```
   Введите ссылку на страницу: https://www.gosuslugi.ru/faq/about_gosuslugi/general
   ```

3. **Скрипт отправит запрос к API, получит данные и сохранит их в текстовые файлы в папке, названной как тема раздела или в `articles` по-умолчанию.**
