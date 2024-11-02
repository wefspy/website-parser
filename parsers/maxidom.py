import requests
from bs4 import BeautifulSoup
from requests import Response

from entities.product import Product

BASE_URL = 'https://www.maxidom.ru/'


def get_products_roof() -> list[Product]:
    response: Response = requests.get(BASE_URL + 'catalog/potolki/')
    soup: BeautifulSoup = BeautifulSoup(response.content, "lxml")

    articles = soup.find_all('article', class_='l-product')
    products: list[Product] = []

    for product in articles:
        name = product.find('span', itemprop='name').get_text(strip=True)
        price = product.find('div', class_='l-product__price-base').get_text(strip=True)
        products.append(Product(name, price))

    return products
