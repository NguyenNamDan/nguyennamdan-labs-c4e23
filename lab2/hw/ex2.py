from urllib.request import urlopen
from bs4 import BeautifulSoup #pip install Bea 
import pyexcel
from collections import OrderedDict
#1 connect to the page
ulr = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
connect = urlopen(ulr)
#2 download content
raw_data = connect.read() 
page_content = raw_data.decode("utf8") # page_content = urlopen(ulr).read().decode("utf8")
#3 find ROI
soup = BeautifulSoup(page_content, "html.parser")
sec = soup.find("table", id= "tableContent")
#4 Bóc data
tr_list = sec.find_all("tr") 
table_list = []
for tr in tr_list:
    td_list= tr.find_all("td")
    diction = {}
    for i in range(len(td_list)):
        if td_list[i].string != None:
            if i==0:
                diction["Hạng mục"]=td_list[i].string.strip()
            elif i==1:
                diction["Qúy 4-2016"]=td_list[i].string.strip()
            elif i==2:
                diction["Quý 1-2017"]=td_list[i].string.strip()
            elif i==3:
                diction["Quý 2-2017"]=td_list[i].string.strip()
            elif i==4:
                diction["Quý 3-2017"]=td_list[i].string.strip()
    if diction != {}:
        table_list.append(diction)  
pyexcel.save_as(records=table_list,dest_file_name="datamilk.xlsx")


