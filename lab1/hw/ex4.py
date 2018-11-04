import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot 
from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
data = client.get_database()
customers = data["customers"]
customers_list = customers.find()
ref_list=[]
ref_count=[]
n = [] 
for cus in customers_list:
    ref_list.append(cus["ref"])
for ref in ref_list:
    while True:
        if ref in n:
            break
        else:
            n.append(ref)
            ref_count.append(ref_list.count(ref))
pyplot.pie(ref_count,labels=n,autopct="%.1f%%",shadow=True)
pyplot.axis("equal")
pyplot.title("references")
pyplot.show()
