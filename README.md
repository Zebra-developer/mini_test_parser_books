# 📚 Book Parser на Python

Парсер с сайта [books.toscrape.com](https://books.toscrape.com), написан на Python с использованием `requests` и `BeautifulSoup`.

### 🔍 Что делает:

- Получает список книг (название, цена, наличие)
- Сканирует до 10 страниц каталога
- Сохраняет данные в CSV-файл

---

## 📦 Используемые библиотеки:

- `requests`
- `bs4`
- `csv`

---

## 🚀 Запуск

```bash
pip install -r requirements.txt
python book_parser.py
