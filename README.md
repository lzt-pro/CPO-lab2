# CPO-lab2

Computational Process Organization lab2 

## Title: StateMachine

eDSL for finite state machine (Moore).

## List of group members

- Zhentao Liu 

  - ID: 192050212
  - Email : lztkystu@163.com

- Shuo Cui

  -  ID: 192050212
  -  Email:13652027261@163.com

  

## Laboratory work number: 3

eDSL for finite state machine (Moore).

- Visualization as a state diagram (GraphViz DOT) or table (ASCII).
- Provide complex an example like a controller for an elevator, crossroad with a traffific light, etc.

## Variant description

eDSL for finite state machine (Moore).

- Visualization as a state diagram (GraphViz DOT) or table (ASCII).
- Provide complex an example like a controller for an elevator, crossroad with a traffific light, etc.

## Synopsis 

- Moore finite state machine - elevator design concept
- Design StateMachine Class
- StateMachineTest
- Input data control 
- StateMachine Visualization
- Conclusion

### Moore finite state machine - elevator design concept

Finite state machine(Moore): The next state is only determined by the current state, i.e. the second state =f(current state, input), and the output =f(current state)

In our work, we try to implement a simple elevator finite state machine. The input state is A_unoverload, A_up. When True, it means the elevator is not overloaded and ascending; When the value is False, it means the elevator is overloaded and descending. The corresponding output is close up, close down, open the door to stop (when overload) three states.

### Design StateMachine Class

arg_type: Restrict input data to a specific type

```python
    def arg_type(num_args, type_args):
        def trace(f):
            def traced(self, *args, **kwargs):
                # print("{}(*{}, **{}) START".format(f.__name__, args, kwargs))
                if type(args[num_args - 1]) == type_args:
                    return f(self, *args, **kwargs)
                else:
                    print("Wrong Input!")
                    print(type(args[num_args - 1]))
                    return 'Wrong Input!'

            return traced

        return trace
```

Args_1: Restrict the length of the input parameter to 1

```python
    def args_1(f):
        def trace(self, *args, **kwargs):
            if len(args) == 1:
                return f(self, *args, **kwargs)
            else:
                print("Wrong Input!")
                return 'Wrong Input!'

        return trace
```

Args_0: Restrict the length of the input parameter to 0

```python
    def args_0(f):
        def trace(self, *args, **kwargs):
            if len(args) == 0:
                return f(self, *args, **kwargs)
            else:
                print("Wrong Input!")
                return 'Wrong Input!'

        return trace
```

### StateMachineTest

Convert_state: To change the elevator's state

```python
    def test_convert_state(self):
        m = StateMachine("convert_state")
        m.input_port("A", latency=1)
        m.output_port("B", latency=1)
        n = m.add_node("convert", lambda a: not a if isinstance(a, bool) else None)
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
```

Add_load: 

```python
 def add_load(a, b):
            n = m.add_node("!{} -> {}".format(a, b), lambda a: not a if isinstance(a, bool) else None)
            n.input(a, latency=1)
            n.output(b, latency=1)
```



add_convert: 

```python
        def add_convert(a, b, c):
            n = m.add_node("{} and {} -> {}".format(a, b, c),
                           lambda a, b: a and b if isinstance(a, bool) and isinstance(b, bool) else None)
            n.input(a, 1)
            n.input(b, 1)
            n.output(c, 1)
```

Elevator: Realize the state transition of elevator

```python
 def test_elevator(self):
        m = StateMachine("elevator")
        m.input_port("A_unoverload",latency=1)
        m.input_port("A_up",latency=1)
        m.output_port("D0_closeup",latency=1)
        m.output_port("D1_closedown", latency=1)
        m.output_port("D2_openstop", latency=1)

        
        def add_load(a, b):
            n = m.add_node("!{} -> {}".format(a, b), lambda a: not a if isinstance(a, bool) else None)
            n.input(a, latency=1)
            n.output(b, latency=1)

        def add_convert(a, b, c):
            n = m.add_node("{} and {} -> {}".format(a, b, c),
                           lambda a, b: a and b if isinstance(a, bool) and isinstance(b, bool) else None)
            n.input(a, 1)
            n.input(b, 1)
            n.output(c, 1)
        add_load("A_unoverload","A_overload")
        add_load("A_up","A_down")
        # True means not overloaded, rising
        # False is overload, down
        add_convert("A_unoverload", "A_up", "D0_closeup")
        add_convert("A_unoverload", "A_down", "D1_closedown")
        add_convert("A_overload", "A_up", "D2_openstop")
        add_convert("A_overload", "A_down", "D2_openstop")
        
```



### Input data control 

In this part, I try to implement the goals: 

- develop a set of decorators, which allows checking input data (types and values);

- decorate all public API of the developed library (see listing 17);

- develop unit tests for checking the modifified library safety.

As we designed in Design StateMachine Class, and we apply them in the function. 

```
 @arg_type(1, str)
    def input_port(self, name, latency=1):
@arg_type(1, str)
    def output_port(self, name, latency=1):
@arg_type(1, str)
    def add_node(self, name, function):
@arg_type(2, int)
    def _source_events2events(self, source_events, clock):
 @args_1
    def _pop_next_event(self, events):
@args_0
    def _state_initialize(self):
@args_0
    def visualize(self):
@arg_type(1, str)
    def input(self, name, latency=1):
@arg_type(1, str)
    def output(self, name, latency=1):
 @arg_type(1, dict)
    def activate(self, state):    

```





### StateMachine Visualization

And in this part I visualize the state machine by this code :

```
				dot = m.visualize()
        f = open('fsm.dot', 'w')
        f.write(dot)
        f.close()

        with open("fsm.dot") as f:
            dot_graph = f.read()
        dot = graphviz.Source(dot_graph)
        dot.view()
```

And it  generates the.dot file as

```
digraph G {
 rankdir=LR;
 A_unoverload[shape=rarrow];
 A_up[shape=rarrow];
 D0_closeup[shape=rarrow];
 D1_closedown[shape=rarrow];
 D2_openstop[shape=rarrow];
 n_0[label="!A_unoverload -> A_overload"];
 n_1[label="!A_up -> A_down"];
 n_2[label="A_unoverload and A_up -> D0_closeup"];
 n_3[label="A_unoverload and A_down -> D1_closedown"];
 n_4[label="A_overload and A_up -> D2_openstop"];
 n_5[label="A_overload and A_down -> D2_openstop"];
 A_unoverload -> n_0;
 A_up -> n_1;
 A_unoverload -> n_2;
 A_up -> n_2;
 n_2 -> D0_closeup;
 A_unoverload -> n_3;
 n_1 -> n_3[label="A_down"];
 n_3 -> D1_closedown;
 A_up -> n_4;
 n_0 -> n_4[label="A_overload"];
 n_4 -> D2_openstop;
 n_0 -> n_5[label="A_overload"];
 n_1 -> n_5[label="A_down"];
 n_5 -> D2_openstop;
}
```

 It generates the .pdf  file as

![image-20200601144948127](/Users/liuzhentao/Library/Application Support/typora-user-images/image-20200601144948127.png)

### Conclusion

- The transition mechanism in Moore finite state machine is very important, which is the key to restrict the input data from the current state to the next state
2. The application of decorator pattern is necessary to effectively limit the format of input data and enhance the robustness of the code
3. Graphviz is a handy tool for data visualization, turning obscure lines of code into readable ones