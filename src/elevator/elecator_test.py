import unittest
from elevator import *
class DiscreteEventTest(unittest.TestCase):
    def test_transition(self):
        inner1 = [2, 3, 4]
        out1 = [3, 4]
        a1 = 0  # overload
        b1 = 1  # layer

        inner2 = [2, 3, 4]
        out2 = [3, 4]
        a2 = 1
        b2 = 1

        inner3 = [3, 4]
        out3 = [4]
        a3 = 0
        b3 = 2

        inner4 = [2, 3]
        out4 = [1, 2]
        a4 = 0
        b4 = 4

        inner5 = [2, 3]
        out5 = [3]
        a5 = 1
        b5 = 4
        m = StateMachine()
        m.add_date(b1, a1, inner1, out1)
        m.add_date(b2, a2, inner2, out2)
        m.add_date(b3, a3, inner3, out3)
        m.add_date(b4, a4, inner4, out4)
        m.add_date(b5, a5, inner5, out5)
        m.transition()
        self.assertEqual(m.outputs,
                         [['OpenStop', 'CloseUp'], 'OpenStop', ['OpenStop', 'CloseUp'], ['OpenStop', 'CloseDown'], 'OpenStop'])