from urllib.request import urlopen
from bs4 import BeautifulSoup #pip install Bea 
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

# PART 1:
#1 connect to the page
ulr = "https://www.apple.com/itunes/charts/songs/"
connect = urlopen(ulr)
#2 download content
raw_data = connect.read() 
page_content = raw_data.decode("utf8")
#3 find ROI
soup = BeautifulSoup(page_content, "html.parser")
sec = soup.find("section","section chart-grid")
ul = sec.div.ul
#4 Bóc data
song_list = ul.find_all("li") 
itunes_list = []
for song in song_list:    
    a1 = song.h3.a
    names = a1.string
    a2 = song.h4.a
    artists = a2.string
    news = OrderedDict({
        "names": names,
        "artists": artists,
    })
    itunes_list.append(news)
pyexcel.save_as(records=itunes_list, dest_file_name="itunes.xlsx")

#PART 2:
options = [
    {
        'default_search': 'ytsearch', 
        'max_downloads': 1 
    },
    {
        'default_search': 'ytsearch', 
        'max_downloads': 1,
        'format': 'bestaudio/audio'
    }
 ]
for song in itunes_list:
    search = [song["names"], "of",song["artists"]]
    dl1 = YoutubeDL(options[0])
    dl1.download(search)
    dl2 = YoutubeDL(options[1])
    dl2.download(search) 

