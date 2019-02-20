from bs4 import BeautifulSoup
import requests
import pytube

url = str(input('Playlist link: '))

response = requests.get(url)
cont = BeautifulSoup(response.text, 'html.parser')
body = cont.body
videos = body.findAll('tr', {'class':'pl-video yt-uix-tile '})

with open('index.txt', 'w') as f:
    for i, video in enumerate(videos):
        title = str(video['data-title'])
        f.write(f't{i} - {title}\n')

