from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#1 Connect
client = MongoClient(uri)
#2 Lay ra database
db = client.get_database()
#3 Lay ra collection
posts = db["posts"]
customers = db["customers"]
#4 Tao ra data


#5 Insert data
#posts.insert_one(new_post)
#movies.insert_one(new_movie)

#5 Read data
post_list = posts.find()
# p = post_list[0]
# print(p["title"]) 
for p in post_list:
    print(p)


#6 Close
client.close() 