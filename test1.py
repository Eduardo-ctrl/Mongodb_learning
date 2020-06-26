from pymongo import MongoClient
from random import randint

conn = MongoClient('localhost',27017)

db = conn.stu

myset = db.class0

cursor = myset.find()
# for i in cursor:
#     myset.update({'_id':i['_id']},{'$set':{'score':\
#         {'chinese':randint(60,100),\
#         'math':randint(60,100),\
#         'english':randint(60,100)\
#         }}},multi = True)

p1 = [{'$group':{'_id':'$gender','count':{'$sum':1}}}]
p2 = [
        {'$match':{'gender':'m'}},
        {'$project':{'_id':0,'name':1,'score.chinese':1}}
     ]
p3 = [
        {'$match':{'gender':'w'}},
        {'$sort':{'score.english':-1}},
        {'$project':{'_id':0,'name':1,'score.english':1}}
     ]  


for x in [p1,p2,p3]:
    cursor = myset.aggregate(x)
    for i in cursor:
        print(i)
    print('------')

conn.close()
