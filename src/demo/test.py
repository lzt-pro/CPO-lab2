from collections import OrderedDict, namedtuple
event = namedtuple("Event", "clock node var val")
source_event = namedtuple("SourceEvent", "var val latency")


if __name__ == "__main__":
    e1 = event(clock=1,node=2,var=3,val=4)
    e2 = event(5,6,7,8)
    # e2._asdict()
    # print(e1.clock)
    # print(e2)

    print("Regular dictionary")
    d = {}
    d['a'] = 'A'
    d['b'] = 'B'
    d['c'] = 'C'
    for k, v in d.items():
        print(k,v)


    print("\nOrder dictionary")
    d1 = OrderedDict()
    d1['a'] = 'A'
    d1['b'] = 'B'
    d1['c'] = 'C'
    d1['1'] = '1'
    d1['2'] = '2'
    for k, v in d1.items():
        print(k,v)

