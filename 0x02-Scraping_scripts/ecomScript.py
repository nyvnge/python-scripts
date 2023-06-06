import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.jumia.co.ke/catalog/?q=Samsung+A32"

HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 
            'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(url, headers=HEADERS)

