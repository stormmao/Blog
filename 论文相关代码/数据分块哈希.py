import hashlib
import time
BLOCKSIZE = 65536                   #就是64kb=1024bit*64
hasher = hashlib.sha1()
ll = []
with open('/Users/maoxiangjie/PycharmProjects/democode/pp4.stp', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)           #迭代哈希，最后的结果和整体哈希的结果是一样的，分块是为了内存友好。
        ll.append(hash(buf))         
        buf = afile.read(BLOCKSIZE)  #每次读取大小为65
print(hasher.hexdigest())
print(ll)
