import redis

r = redis.Redis(host = 'redis', port = 6379, db = 1)
r.set('k1', 'v1')
r.set('k2', 'v2')
print(r.get('k1'))
print(r.keys())
#打印当前所有的keys
print(r.dbsize())
#查看当前有多少keys
r.delete('k2')
#删除k2
print(r.keys())
print(r.dbsize())
print(dir(r))
#查看redis对应的方法

'''
采用pipeline方式
一次性批量提交命令
'''
# #pipeline
p = r.pipeline()
p.set('k3', 'v3')
p.set('k4', 'v4')
p.incr('num')
p.incr('num')
p.execute()
print(r.get('num'))
