# -*- coding: utf-8 -*
from bs4 import BeautifulSoup
broken_html = '<ul class=country><li>Area</li>Population</ul>'
soup = BeautifulSoup(broken_html, 'html.parser')
fixed_html = soup.prettify()
print fixed_html
