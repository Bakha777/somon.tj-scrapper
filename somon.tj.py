from urllib.request import urlopen
from bs4 import BeautifulSoup


def extract_info(soup):
    res = []

    bs4_titles = soup.find_all('a', 'advert__content-title')

    for title in bs4_titles:
        data = title.text.strip().split(', ')
        res.append({
            'name': data[0],
            'year': data[1],
        })

    bs4_prices = soup.find_all('a', 'advert__content-price _not-title')

    index = 0
    for title in bs4_prices:
        data = title.text.strip().split(', ')
        if index < len(res):
            res[index]['price'] = data[0]
        index += 1

    return res


for i in range(10):
    url = f'https://somon.tj/transport/legkovye-avtomobili/?page={i}'
    html_content = urlopen(url)
    soup = BeautifulSoup(html_content, 'html.parser')

    result = extract_info(soup)



url = 'https://somon.tj/transport/legkovye-avtomobili/'
html_content = urlopen(url)
soup = BeautifulSoup(html_content, 'html.parser')

res = extract_info(soup)

print(f'Your result: {url}')
print(res)

