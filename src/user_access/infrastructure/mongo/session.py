from pymongo import MongoClient


host = "mongo"
port = 27017
id = "root"
password = "qwerqwer123"
connection = MongoClient(f'mongodb://{id}:{password}@{host}:{port}/admin')
