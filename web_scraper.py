import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithtomi.com/'

request = requests.get(url)

soup = BeautifulSoup(request.content, 'lxml')
titles = soup.findAll('h2', {'class':'post-title'})

titles = [title.getText() for title in titles]

for t in titles:    
    print(t)