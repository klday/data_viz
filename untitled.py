#Script for getting nobel-prize data into mongodb
from pymongo import MongoClient
import requests

def main():
    nobel_winners = [
        {'category':'Physics',
         'name':'Albert Einstein',
         'nationality':'Swiss',
         'sex':'male',
         'yeaer':1921},
        {'category':'Physics',
         'name':'Paul Dirac',
         'nationality':'British',
         'sex':'male',
         'yeaer':1933},
        {'category':'Chemistry',
         'name':'Marie Curie',
         'nationality':'Polish',
         'sex':'female',
         'yeaer':1911}]

    client = MongoClient()
    DB_NOBEL_PRIZE = 'nobel_prize'
    COLL_WINNERS = 'winners'
    db = client[DB_NOBEL_PRIZE]
    coll = db[COLL_WINNERS]
    coll = db.winners

    db = get_mongo_database(DB_NOBEL_PRIZE)
    coll = db[COLL_WINNERS]
    coll.insert(nobel_winners)

    return

def get_mongo_database(db_name,host='localhost',port=27017,username=None,password=None):
    """
    Get named database from MongoDB without authentication.
    """
    #make Mongo connection without authentication
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s/%s'%(username, password, host, db_name)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)

    return conn[db_name]
