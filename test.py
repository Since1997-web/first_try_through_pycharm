import pymongo
client = client = pymongo.MongoClient("mongodb+srv://satya:Satya123@cluster0.etwg9.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "satya",
    "email" :"satyapadhiary@gmail.com",
    "surname" :"padhiary"

}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)