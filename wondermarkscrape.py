import requests
from bs4 import BeautifulSoup
givendir = raw_input("Enter the path where the images should be stored!\n")
r = requests.get("http://wondermark.com/001/")
counter = 1
while True:
    soup = BeautifulSoup(r.text, 'html.parser')
    imglink = soup.find(id="comic").img['src']
    print imglink
    q = requests.get(imglink)
    with open(givendir+"/"+str(counter).zfill(4)+"."+imglink[-3:], 'wb') as fd:
        for chunk in q.iter_content():
            fd.write(chunk)
    print soup.find(id="comic-right").div.a['href']
    r = requests.get(soup.find(id="comic-right").div.a['href'])
    counter += 1
