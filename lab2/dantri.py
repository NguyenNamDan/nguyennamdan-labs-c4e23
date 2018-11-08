from urllib.request import urlopen
from bs4 import BeautifulSoup #pip install Bea 
import pyexcel 
from collections import OrderedDict
#1 connect to the page 
ulr = "https://dantri.com.vn"
connect = urlopen(ulr) 

#2 download content
raw_data = connect.read() 
page_content = raw_data.decode("utf8")

with open("dantri.html", "w") as f: #Save
    f.write(page_content)
#3 find ROI
soup = BeautifulSoup(page_content, "html.parser")
ul = soup.find("ul", "ul1 ulnew") #tìm thẻ 


#4 Extract data 
li_list = ul.find_all("li")
new_list = []
for li in li_list:    
    a = li.h4.a
    title = a.string  
    link = ulr + a["href"]  

    news = OrderedDict({
        "title": title,
        "link": link,
    })
    new_list.append(news)
    print(new_list)  
pyexcel.save_as(records=new_list, dest_file_name="dantri.xlsx")

#5 save data 
