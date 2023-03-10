import requests
import json
import pymongo
import string
import random

client = pymongo.MongoClient("mongodb+srv://employee:ccoffee@chamberlaincoffee.wi9qrir.mongodb.net/?retryWrites=true&w=majority")
db = client.products

def mongodbGet():
  mycollection = db["products"]
  all_reconds = mycollection.find()
  list_cursor = list(all_reconds)
  return list_cursor
  
def mongodbInsert(newname,newcost,newimage):

  S = 10
  ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
  product = {"productid": ran, "name": newname, "cost":newcost, "image":newimage }
  db.products.insert_one(product)

def mongodbDelete(deleteid):
  delete = {"productid": deleteid}
  db.products.delete_one(delete)

def mongodbFind(findid):
  result = db.products.find_one({"productid": findid})
  return result

def mongodbUpdate(updateid,updatename,updatecost,updateimage):
  filter = {"productid": updateid}
  newvalues = { "$set":{"name": updatename, "cost":updatecost, "image":updateimage } }
  db.products.update_one(filter, newvalues, True)
  