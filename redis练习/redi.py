import redis
from time import *

pool= redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)
r=redis.Redis(connection_pool=pool) #建立连接池，避免频繁连接和断开带来的性能损耗
r.set('foo', 'ok',ex=3)
print(r['foo'])
sleep(1)
print(type(r['foo']))
print(r['foo'])

