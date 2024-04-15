from bs4 import BeautifulSoup
import requests
import json
import re
from datetime import datetime
import subprocess

def commit_and_push_changes():
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Update data"])
    subprocess.run(["git", "push"])

html = requests.get('https://news.republika.co.id/')
soup = BeautifulSoup(html.text, 'html.parser')

infoNews = []
infoNewsSpecial = []

for i in soup.find_all('div', class_='caption'):
    time_element = i.find_next('div', class_='date')   # mencari elemen waktu publikasi
    waktu_publish = (time_element.text.split('-')[1].strip() if time_element
                     else (i.find("small").text.strip() if i.find("small")
                           else 'Unknown'))
    kategori = (i.find_next('span', class_='kanal-info').text if i.find_next('span', class_='kanal-info')
                else 'Terpopuler')
    judul = (i.find('h3').text.strip() if i.find('h3')
             else (i.find(class_='title').text.strip() if i.find(class_='title')
                   else 'Tidak ada judul'))
    infoNew = {
        'judul': judul,
        'kategori': kategori,
        'waktu_publish': waktu_publish,
        'waktu_scraping': datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }
    if re.match(r'\w+ , \d{2} \w+ \d{4}, \d{2}:\d{2}', waktu_publish):
        infoNewsSpecial.append(infoNew)
    else:
        infoNews.append(infoNew)

with open('info.json', 'w') as f:
    json.dump(infoNews, f)



commit_and_push_changes()
