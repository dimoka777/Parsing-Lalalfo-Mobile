from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv


def main():
    # url = 'https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary/mobilnye-telefony'
    # html = urlopen(url)
    html = open('index.html').read()
    bsoup = BeautifulSoup(html, features="html.parser")

    ads = bsoup.find_all('article', class_='listing-item')
    total_price = []
    total_title = []
    total_image = []
    result = []
    for ad in ads:
        try:
            price = ad.find('div', class_='listing-item-main').find('p', class_='listing-item-title')
            price_get = price.get_text().replace('\n', '').replace('\xa0', ' ')
            total_price.append(price_get.strip())

            title = ad.find('div', class_='listing-item-main').find('a', class_='listing-item-title')
            title_get = title.get_text()
            total_title.append(title_get.strip())

            image = ad.find('div', class_='listing-item-img-wrap').find('img', class_='listing-item-photo link-image')
            image_get = image.get('data-url')
            total_image.append(image_get)

            result.append([price_get.strip(), title_get.strip(), image_get])

        except Exception as e:
            print(e)
    # print(total_price, '\n', total_title, '\n', total_image)
    print(result)

    with open('lalafo', 'w') as lala_file:
        writer = csv.writer(lala_file, quoting=csv.QUOTE_NONE, delimiter='|',
                            quotechar='', escapechar='\\')
        for row in result:
            writer.writerow(row)
    lala_file.close()


if __name__ == '__main__':
    main()