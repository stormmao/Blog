#hash.py
import hashlib
import hashlib
import time
start = time.time()
BLOCKSIZE = 65536                   #就是64kb=1024bit*64
hasher = hashlib.sha1()
ll = []
with open('/Users/maoxiangjie/PycharmProjects/democode/pp4.stp', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        ll.append(hash(buf))
        buf = afile.read(BLOCKSIZE)  #每次读取大小为65

print(hasher.hexdigest())
print(ll)
print("run time is :%s",time.time()-start) #计算程序运行时间


#Sha1andMd5.py
import sys
import hashlib

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

md5 = hashlib.md5()
sha1 = hashlib.sha1()

with open(sys.argv[1], 'rb') as f: #直接从 Terminal 传入命令运行  python Sha1andMd5.py pp4.stp
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        md5.update(data)
        sha1.update(data)

print("MD5: {0}".format(md5.hexdigest()))
print("SHA1: {0}".format(sha1.hexdigest()))


