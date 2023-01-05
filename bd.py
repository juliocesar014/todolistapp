from pymongo import MongoClient
from pw import pw
####### PW = Your password user in MongoDB Atlas ######

cluster = MongoClient(f"mongodb+srv://julio-todolistapp:{pw}@cluster0.hmjcxgi.mongodb.net/?retryWrites=true&w=majority")

db = cluster["todolistapp"]
collection = db["todo"]


## Test my App connect with MongoDB Atlas

##collection.insert_one({"tasks":"Exemplo de task 01"})