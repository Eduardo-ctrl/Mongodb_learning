#将文件以grid方案存放到数据库

from pymongo import MongoClient
import gridfs

conn = MongoClient('localhost',27017)

db = conn.grid

#获取gridfsf对象
fs = gridfs.GridFS(db)

files = fs.find()

for file in files:
    print(file.filename)
    if file.filename == 'mm.png':
        with open(file.filename,'wb') as f:
            #从数据库读取内容
            data = file.read()
            #写入到本地
            f.write(data)
conn.close()