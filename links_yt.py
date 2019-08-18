import requests
import bs4
import sys
import os

# pyhton3 links_yt.py <search>
q = ''
if(len(sys.argv) > 1):
    if(len(sys.argv) == 2):
        q = sys.argv[1]
        q = '+'.join(q.split(' '))
    else:
        q = sys.argv[1:]
        q = '+'.join(q)
s = 'https://www.youtube.com'
site = 'https://www.youtube.com/results?search_query='+q
plist = []
i = 0

res = requests.get(site)
soup = bs4.BeautifulSoup(res.text,'lxml')
for link in soup.find_all('a',href=True):
    if(link['href'][:6] == '/watch'):
        try:
            print( str(i) + ' : ' +  link['title'])
            i+=1
        except:
            plist.append(link['href'])

ind = int(input())
os.system('mpv ' + '\'' + s + plist[ind] + '\'')
