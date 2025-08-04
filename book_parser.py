import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# берем данные книги 
def get_books_from_page(page_number):
    url = BASE_URL.format(page_number)
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for book in soup.select(".product_pod"):
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text.strip()
        availability = book.select_one(".instock.availability").text.strip()
        books.append({
            "title": title,
            "price": price,
            "availability": availability
        })

    return books

# функция скрапинка книг
def scrape_all_books(pages=5):
    all_books = []
    for page in range(1, pages + 1):
        print(f"📄 Сканирую страницу {page}...")
        books = get_books_from_page(page)
        all_books.extend(books)
    return all_books

# функция сохранения списка книг в csv файл
def save_to_csv(books, filename="books.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price", "availability"])
        writer.writeheader()
        writer.writerows(books)
    print(f"✅ Сохранено {len(books)} книг в файл {filename}")


if __name__ == "__main__":
    books_data = scrape_all_books(pages=10)  # можно увеличить до 50
    save_to_csv(books_data)
