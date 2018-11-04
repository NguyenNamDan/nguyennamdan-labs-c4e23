from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
data = client.get_database()
posts = data["posts"]
new_post = {
    "title": "Teckids - Coding school",
    "author": "Nguyen Nam Dan",
    "content": '''
    e mong muốn trong thời gian tới, Techkids có thể khôi phục lại khoá IOS đã từng là khoá học được ưa thích nhất Techkids.
    Cảm ơn Techkids <3.
    ''',
}
posts.insert_one(new_post)
client.close() 


