import requests
from bs4 import BeautifulSoup

url = 'https://www.ag-grid.com/javascript-data-grid/grid-events/'
parts = url.split('://')
domain = parts[1].split('/')[0]
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    elements_to_scrape = ['p', 'span', 'div', 'h1']

    extracted_text = []

    for element_name in elements_to_scrape:
        elements = soup.find_all(element_name)
        for element in elements:
            text = element.get_text()
            extracted_text.append(text)

    with open(domain+".txt", 'w', encoding='utf-8') as file:
        for text in extracted_text:
            file.write(text + '\n')

else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
