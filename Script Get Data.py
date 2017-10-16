import requests
from bs4 import BeautifulSoup

months=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

for year in range (1999, 2015):
    for month in months:
        url='https://www.ecb.europa.eu/pub/pdf/mobu/mb'+str(year)+month+'en.pdf'
        data=requests.get(url, stream=True).content
        with open(str(year)+ ' '+month+'.pdf', "wb") as f:
            f.write(data)
            print ("Done...")
