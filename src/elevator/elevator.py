import graphviz

def findmaxmin(innerAn, outAn):
    max1 = max(innerAn, key=abs)
    min1 = min(innerAn)
    max2 = max(outAn)
    min2 = min(outAn)
    minf = min(min1,min2)
    maxf = max(max1,max2)
    return minf,maxf
class StateMachine:
    def __init__(self,name = "too hard"):
        self.name = name
        self.state = None
        self.nextstate = None
        self.inputs = []
        self.outputs = [] # Output state
        self.active = [] # Execution action
    def add_state(self,state):
        self.state = state
    def add_node(self,node):
        self.inputs.append(node)
    # def add_date(self,*args):
    #     self.current_left = args[0]
    #     self.overload = args[1]
    #     self.innerAn = args[2]
    #     self.outAn  = args[3]
    #     self.inputs.append([self.state,self.current_left,self.overload,self.innerAn,self.outAn])
    # State transition
    def transition(self):
        for date in self.inputs:
            if date.overload == 1:
                self.outputs.append([date.name,"OpenStop"])
            else:
                if date.state == "OpenStop":
                    min, max = findmaxmin(date.innerAn, date.outAn)
                    if date.current_left > max:
                        self.outputs.append([date.name,"CloseDown"])
                        self.active.append("down to " + str(max) + "floor")
                        self.nextstate = "CloseUp"
                    if date.current_left < min:
                        self.outputs.append([date.name,"CloseUp"])
                        self.active.append("up to " + str(min) + "floor")
                        self.nextstate = "CloseDown"


    # visualization
    def visualize(self):
        res = []
        res.append("digraph G {")
        res.append("   rankdir=LR;")
        node = []

        for node in self.inputs:
            res.append('   {}[];'.format(node.name))
            # res.append(" {}[The current layer];".format(current))
            # res.append(" {}[The current overload];".format(overload))
            # res.append(" {}[The button in the elevator];".format(innerAn))
            # res.append(" {}[The dictionary outside the elevator];".format(innerAn))
            # node.append(self.inputs[0])
        # for v in self.outputs:
        #     res.append('   {}[];'.format(v))
        for i in self.outputs:
            res.append('   {} -> {}[];'.format(i[0], i[1]))

        res.append("}")
        return "\n".join(res)
class Node:
    def __init__(self,name="node",layer=0,overload=0,inner=[],out=[]):
        self.name = name
        self.state = "OpenStop"
        self.current_left = layer
        self.overload = overload
        self.innerAn = inner  # Elevator interior button
        self.outAn = out  # Elevator external button
if __name__ == "__main__":
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

    inner6 = [4, 3]
    out6 = [3]
    a6 = 0
    b6 = 2

    inner7 = [4, 3]
    out7 = [3]
    a7 = 1
    b7 = 2

    inner8 = [2]
    out8 = [1, 2]
    a8= 0
    b8 = 3
    m = StateMachine()
    node1 = Node("S0", b1, a1, inner1, out1)
    node2 = Node("S1", b2, a2, inner2, out2)
    node3 = Node("S2", b3, a3, inner3, out3)
    node4 = Node("S3", b4, a4, inner4, out4)
    node5 = Node("S4", b5, a5, inner5, out5)
    node6 = Node("S5", b6, a6, inner6, out6)
    node7 = Node("S6", b7, a7, inner7, out7)
    node8 = Node("S7", b8, a8, inner8, out8)
    # m.add_date(b1,a1,inner1,out1)
    # m.add_date(b2, a2, inner2, out2)
    # m.add_date(b3, a3, inner3, out3)
    # m.add_date(b4, a4, inner4, out4)
    # m.add_date(b5, a5, inner5, out5)
    m.add_node(node1)
    m.add_node(node2)
    m.add_node(node3)
    m.add_node(node4)
    m.add_node(node5)
    m.add_node(node6)
    m.add_node(node7)
    m.add_node(node8)
    m.transition()
    dot = m.visualize()
    f = open('fsm.dot', 'w')
    f.write(dot)
    f.close()

    with open("fsm.dot") as f:
        dot_graph = f.read()
    dot = graphviz.Source(dot_graph)
    dot.view()

