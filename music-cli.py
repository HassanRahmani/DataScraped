from bs4 import BeautifulSoup
import requests 
from os import system

while True:
    headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
    print('[*]Only for LINUX... Download mpv also')
    song = input('> ')
    song_query = song.replace(' ','%20')

    r = requests.get(f'https://soundcloud.com/search?q={song_query}',headers=headers)
    soup = BeautifulSoup(r.text,'html.parser')
    all_links = []
    for link in soup.find_all('a',href=True):
        hrefs = link.get('href')
        all_links.append(hrefs)
        
    href_link = all_links[6]
    complete_link = 'https://soundcloud.com'+href_link
    system('mpv '+complete_link)
