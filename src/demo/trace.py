def inc(a,**kwargs):
    for key in kwargs:
        b = kwargs[key]
    return  a+b
def trace(f):
    def traced(*args, **kwargs):
        print("{}(*{}, **{}) START".format(f.__name__, args, kwargs))
        try:
            return f(*args, **kwargs)
        finally:
            print("{} FINISH".format(f.__name__))
    return traced
# # print(inc(10,11))
# traced_inc = trace(inc)
# print(traced_inc(10,li=111))
@trace
def dec(a):
    print(a-1)
class Foo(object):
    @trace
    def foo(self):
        print('hello')
dec(10)
Foo().foo()