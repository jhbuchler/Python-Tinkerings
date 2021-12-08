import bs4
import requests

payload={}
headers = {
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4736.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-dest': 'document'
}    
    

url = ('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_3?crid=BQC7B6QWO7HS&keywords=automate+the+boring+stuff+with+python&qid=1638575048&sprefix=automate+the+bo%2Caps%2C187&sr=8-3')

res = requests.request('GET', url, headers=headers, data=payload)

soup = bs4.BeautifulSoup(res.text, 'lxml')

price = soup.select('#newBuyBoxPrice')[0].contents[0]
print(price)
