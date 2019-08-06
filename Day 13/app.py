from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["data1"]

collection = db["test"]



def add_new_faculty():
    
    rec1 = {"name" : "Manoj","age" : 38.0,"gender" : "M", 	"subjects" : [ "JAVA", "DBMS"	], "type" : "Full Time","qualification" : "Ph.D","exp" : 12.0}
    print('Success')
    
    collection.insert_one(rec1)

def add_subject_to_faculty():
    collection.update_one({'name':"Manoj"},{"$push":{"subjects":"ML"}})


def remove_subject_from_faculty():
    collection.update_one({"name":"Manoj"}, {"$pull":{"subjects":"JAVA"}})


def increment_exp_by_one_year():
    collection.update_one({"name":"Manoj"}, {"$inc": {"exp":1, "age":1}})


def update_qualification():
    collection.update_one({"name":"Manoj"}, {"$set":{"qualification":"M.tech"}})

def total_duration_by_faculty():
    pipe = [{"$group":{"_id":"null", "res":{"$sum":"$exp"}}},{"$project":{"_id":"0"}}]
    print(collection.aggregate(pipe))

def subject_with_faculty_name():
    x = collection.aggregate([{"$project":{"name":"$name","subjects":1, "_id":0}}])
    for i in x:
        print(i)

def delete_faculty():
    collection.delete_one({"name":"Manoj"})

subject_with_faculty_name()