import collections
print("Regular dictionary")
d={}
d['a']='A'
d['b']='B'
d['c']='C'
d['1'] = '1'
for k,v in d.items():
    print (k,v)

print("\nOrder dictionary")
d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['c'] = 'C'
d1['1'] = '1'
d1['b'] = 'B'
d1['2'] = '2'
for k,v in d1.items():
    print(k,v)

a = lambda x : x*x
print(a(2))
b = lambda a: not a if isinstance(a, bool) else None


# https://www.runoob.com/python/python-func-zip.html zip用法
# https://www.runoob.com/python/python-func-isinstance.html isinstance用法
# https://www.cnblogs.com/baxianhua/p/10406406.html nametuple
# https://www.runoob.com/python/python-tuples.html 元组