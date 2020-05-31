import unittest
from disevent import *
class DiscreteEventTest(unittest.TestCase):
    def test_logic_not(self):
        m = DiscreteEvent("logic_not")
        m.input_port("A", latency=1)
        m.output_port("B", latency=1)
        n = m.add_node("not", lambda a: not a if isinstance(a, bool) else None)
        n.input("A", latency=1)
        n.output("B", latency=1)
        m.execute(
         source_event("A", True, 0),
         source_event("A", False, 5),
         )
        self.assertEqual(m.state_history, [
         (0, {'A': None}),
         (2, {'A': True}),
         (4, {'A': True, 'B': False}),
         (7, {'A': False, 'B': False}),
         (9, {'A': False, 'B': True}),
         ])
        self.assertListEqual(m.event_history, [
         event(clock=2, node=n, var='A', val=True),
         event(clock=4, node=None, var='B', val=False),
         event(clock=7, node=n, var='A', val=False),
         event(clock=9, node=None, var='B', val=True),
         ])
        # dot = m.visualize()
        # f = open('fsm.dot', 'w')
        # f.write(dot)
        # f.close()
        #
        # with open("fsm.dot") as f:
        #     dot_graph = f.read()
        # dot = graphviz.Source(dot_graph)
        # dot.view()
    def test_decoder(self):
        m = DiscreteEvent("2-4-decoder")
        m.input_port("A0", latency=1)
        m.input_port("A1", latency=1)
        m.output_port("D0", latency=1)
        m.output_port("D1", latency=1)
        m.output_port("D2", latency=1)
        m.output_port("D3", latency=1)
        def add_not(a, b):
            n = m.add_node("!{} -> {}".format(a, b), lambda a: not a if isinstance(a, bool) else None)
            n.input(a, latency=1)
            n.output(b, latency=1)
        def add_and(a, b, c):
            n = m.add_node("{} and {} -> {}".format(a, b, c),
                    lambda a, b: a and b if isinstance(a, bool) and isinstance(b, bool) else None)
            n.input(a, 1)
            n.input(b, 1)
            n.output(c, 1)
        add_not("A0", "notA0")
        add_not("A1", "notA1")
        add_and("notA0", "notA1", "D0")
        add_and("A0", "notA1", "D1")
        add_and("notA0", "A1", "D2")
        add_and("A0", "A1", "D3")
        test_data = [
             ({'A1': None, 'A0': False}, {'D3': None, 'D2': None, 'D1': None, 'D0': None}),
             ({'A1': False, 'A0': False}, {'D3': False, 'D2': False, 'D1': False, 'D0': True}),
             ({'A1': False, 'A0': True}, {'D3': False, 'D2': False, 'D1': True, 'D0': False}),
             ({'A1': True, 'A0': False}, {'D3': False, 'D2': True, 'D1': False, 'D0': False}),
             ({'A1': True, 'A0': True}, {'D3': True, 'D2': False, 'D1': False, 'D0': False})
                ]
        for a, d in test_data:
            source_events = [source_event(k, v, 0) for k, v in a.items()]
            actual = m.execute(*source_events)
            expect = {}
            expect.update(actual)
            expect.update(d)
            self.assertEqual(actual, expect)
        # dot = m.visualize()
        # f = open('fsm.dot', 'w')
        # f.write(dot)
        # f.close()
        #
        # with open("fsm.dot") as f:
        #     dot_graph = f.read()
        # dot = graphviz.Source(dot_graph)
        # dot.view()
class NodeTest(unittest.TestCase):
    def test_logic_not(self):
        n = Node("not", lambda a: not a if isinstance(a, bool) else None)
        n.input("A", 1)
        n.output("B", 1)
        test_data = [
         (False, True),
         (False, True),
         (None, None),
         ]
        for a, b in test_data:
            self.assertEqual(n.activate({"A": a}), [source_event("B", b, 1)])
    def test_logic_and(self):
        n = Node("and", lambda a, b: a and b if isinstance(a, bool) and isinstance(b, bool) else None)
        n.input("A", 1)
        n.input("B", 1)
        n.output("C", 1)
        test_data = [
         (None, False, None),
         (False, False, False),
         (True, False, False),
         (False, True, False),
         (True, True, True),
         ]
        for a, b, c in test_data:
            self.assertEqual(n.activate({"A": a, "B": b}), [source_event("C", c, 1)])
    def test_1_to_2_decoder(self):
        def decoder(a):
            if a == 0: return (0, 1)
            if a == 1: return (1, 0)
            return (None, None)
        n = Node("decoder", decoder)
        n.input("A", 1)
        n.output("D1", 1)
        n.output("D0", 2)
        test_data = [
         (0, 0, 1),
         (1, 1, 0),
         (None, None, None),
         ]
        for a, d1, d0 in test_data:
            self.assertEqual(n.activate({"A": a}), [source_event("D1", d1, 1), source_event("D0", d0, 2)])
if __name__ == '__main__':
 unittest.main()