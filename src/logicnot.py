
m = DiscreteEvent("logic_not")
m.input_port("A", latency=1)
m.output_port("B", latency=1)
n = m.add_node(lambda a: not a if isinstance(a, bool) else None)
n.input("A", latency=1)
n.output("B", latency=1)