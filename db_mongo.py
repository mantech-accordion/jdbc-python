# import jaydebeapi, os
from pymongo import MongoClient
import datetime
import pprint

def new_posts():
    new_posts = [{"author": "Mike",
               "text": "Another post!",
               "tags": ["bulk", "insert"],
               "date": datetime.datetime(2009, 11, 12, 11, 14)},
              {"author": "Eliot",
               "title": "MongoDB is fun",
               "text": "and pretty easy too!",
               "date": datetime.datetime(2009, 11, 10, 10, 45)}]

    return new_posts

def post():

    post = {"author": "Bskim",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}

    return post

def db_mongo(dir):

    username = 'root'
    password = 'root'
    mongo_url = '10.20.200.111:32427'
    client = MongoClient('mongodb://%s:%s@%s' % (username, password,mongo_url))

    ## Create Database 'test' 

    db = client.test_database
    # or 
    # db = client['test-database']
    
    # print(db)
    # print(dir(db))
    # print(db.name)

    ## Getting a Collection
    collection = db.test_collection
    # or 
    # collection = db['test-collection']

    # print(collection)
    # print(dir(collection))

    # Getting a Collection 'posts'
    posts = db.posts
    # post_id = posts.insert_one(dir).inserted_id
    result = posts.insert_many(new_posts)
    print(result.inserted_ids)

    # pprint.pprint(posts.find_one())
    # pprint.pprint(posts.find_one({"author": "Bskim"}))


    # for post in posts.find():
    #    pprint.pprint(post)

    
    d = datetime.datetime(2009, 11, 12, 12)

    for post in posts.find({"date": {"$lt": d}}).sort("author"):
        pprint.pprint(post)

    print('Count documents - ',posts.count_documents({}))

# Run Interpreter
# if __name__ == "__main__":
post = post()
new_posts = new_posts()
db_mongo(new_posts)