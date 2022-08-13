import csv
import json
from time import sleep
import requests
import os

from config import headers, proxy


def write_csv(city):
    f = open('all_product.json', encoding='utf8')
    with open('data_product.csv', 'a', newline='') as file:
        data = json.load(f)
        writer = csv.writer(file, delimiter=';')
        for i in range(len(data)-1):
            try:
                dict_prod = [
                    data[i]['id'],
                    data[i]['title'],
                    data[i]['old_price']['price'],
                    city,
                    data[i]['price']['price'],
                    data[i]['link']['web_url']
                ]
                writer.writerow(dict_prod)
            except:
                dict_prod = [
                    data[i]['id'],
                    data[i]['title'],
                    data[i]['price']['price'],
                    city,
                    "NULL",
                    data[i]['link']['web_url']
                ]
                writer.writerow(dict_prod)
    f.close()


def parse_all_products(headers):
    f = open('all_product.json', encoding='utf8')
    with open('data_product.csv', 'a', newline='') as file:
        data = json.load(f)
        headers_data = ['id', 'name', 'price', 'city', 'promo_price', 'link']
        writer = csv.writer(file, delimiter=';')
        writer.writerow(headers_data)

    for i in range(30, 540, 30):
        url = f"https://api.detmir.ru/v2/products?filter=categories[].alias:lego;promo:false;withregion:RU-SPE&expand=meta.facet.ages.adults,meta.facet.gender.adults,webp&meta=*&limit=30&offset={i}&sort=popularity:desc"
        response = requests.get(url, headers=headers,
                                timeout=10, proxies=proxy)
        products = response.json()['items']
        json_products = json.dumps(products, indent=4, ensure_ascii=False)
        with open('all_product.json', 'w', encoding='utf8') as file:
            file.write(json_products)
        write_csv('Saint Petersburg')
        print('30 products append')
        sleep(10)

    for i in range(30, 540, 30):
        url = f"https://api.detmir.ru/v2/products?filter=categories[].alias:lego;promo:false;withregion:RU-MOW&expand=meta.facet.ages.adults,meta.facet.gender.adults,webp&meta=*&limit=30&offset={i}&sort=popularity:desc"
        response = requests.get(url, headers=headers,
                                timeout=10, proxies=proxy)
        products = response.json()['items']
        json_products = json.dumps(products, indent=4, ensure_ascii=False)
        with open('all_product.json', 'w', encoding='utf8') as file:
            file.write(json_products)
        write_csv('Moscow')
        print('30 products append')
        sleep(10)


def main():
    parse_all_products(headers)
    os.remove('all_product.json')


if __name__ == '__main__':
    main()
