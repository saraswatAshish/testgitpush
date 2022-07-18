import pymongo

client = pymongo.MongoClient("mongodb+srv://ashish:ashish@cluster0.83kj4yk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "saraswat",
    "email": "ashish@gmail.ai",
    "surname": "ashish"
    }
d = {
    "name": "saraswat",
    "email": "ashish@gmail.ai",
    "surname": "ashish"
    }
d = {
    "name": "saraswat",
    "email": "ashish@gmail.ai",
    "surname": "ashish"
    }
d = {
    "name": "saraswat",
    "email": "ashish@gmail.ai",
    "surname": "ashish"
    }
d = {
    "name": "saraswat",
    "email": "ashish@gmail.ai",
    "surname": "ashish"
    }
d = {
    "name": "saraswat",
    "email": "ashish@gmail.ai",
    "surname": "ashish"
    }
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)