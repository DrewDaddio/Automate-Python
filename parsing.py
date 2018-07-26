# Parsing HTML: Webscraping

# Module beautifulsoup4 - in order to webscrape
import bs4

import requests
res = requests.get('https://www.humblebundle.com/books/linux-geek-books?hmb_source=humble_home&hmb_medium=product_tile&hmb_campaign=mosaic_section_1_layout_index_1_layout_type_twos_tile_index_2')
res.raise_for_status()
# The 'html.parser' stops a "warning" message on python showing
soup = bs4.BeautifulSoup(res.text, 'html.parser')
soup.select('<td class="st-td js-statistics-total-payments">$72,765.36</td>')
elems = soup.select('<td class="st-td js-statistics-total-payments">$72,765.36</td>')

print(elems[0].text)
print(elems[0].text.strip())

