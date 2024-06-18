import requests
from bs4 import BeautifulSoup
import json
from datetime import date
from datetime import datetime
#req ke website
page = requests.get("https://www.republika.co.id/")

# Extract konten menjadi objek BeautifulSoup
soup =  BeautifulSoup(page.text, 'html.parser')#seluruh data web dalam bentuk html

#mempersempit data pada ruang lingkup class list-group wrap-latest, masih dalam format html
rawData = soup.find(class_='list-group wrap-latest')
#mempersempit data pada ruang lingkup class caption, sudah dalam format string
rawCapts = rawData.find_all(class_='caption')
#mempersempit data yang ada pada rawData dalam ruang lingkup class date, sudah dalam format string
rawCatsNDates = rawData.find_all(class_='date')

#transformasi data menjadi array dan memisahkan antara data yang berisikan kategori dan tanggal dengan judul
rawCapts = [capts.text.strip().split('\n') for capts in rawCapts]
#transformasi data menjadi array dengan memisahkan antara data yang berisikan kategori dan data yang berisikan tanggal
CatsNDates = [date.text.strip().split("-") for date in rawCatsNDates]
#mengambil data-data yang berisikan judul pada rawCaption
capts = [capt[1] for capt in rawCapts]
#mengambil data-data yang berisikan kategori pada CatsNDates
cats = [cat[0] for cat in CatsNDates]
#mengambil data-data yang berisikan waktu penayangan pada CatsNDates
dates = [date [1] for date in CatsNDates]
#variabel yang nantinya menampung data-data berita dalam bentuk yang sama dengan format json
today = date.today()#mengambil tanggal terkini
thisTime = datetime.now()#mengambil waktu terkini
jsonForm = []
for i in range(0,len(dates),1):
    jsonForm.append({"kategori":cats[i],"judul":capts[i],"waktu":dates[i],"update":str(today)+" | "+thisTime.strftime("%H:%M")})#memasukkan setiap data kedalam penampung

with open ("dataBerita.json","w") as updateBerita:
    json.dump(jsonForm,updateBerita)#memasukkan data yang sudah ditampung kedalam json file 