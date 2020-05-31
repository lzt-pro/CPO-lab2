# CPO-lab2

Computational Process Organization lab2 

## title: StateMachine

eDSL for finite state machine (Moore).

- Visualization as a state diagram (GraphViz DOT) or table (ASCII).
- Provide complex an example like a controller for an elevator, crossroad with a traffific light, etc.

## list of group members

- Zhentao Liu 

  - ID: 192050212
  - Email : lztkystu@163.com

- Shuo Cui

  -  ID: 192050212
  -  Email:13652027261@163.com

  

## laboratory work number: 3

## variant description

eDSL for finite state machine (Moore).

- Visualization as a state diagram (GraphViz DOT) or table (ASCII).
- Provide complex an example like a controller for an elevator, crossroad with a traffific light, etc.

## synopsis 

Finite state machine(Moore): The next state is only determined by the current state, i.e. the second state =f(current state, input), and the output =f(current state)

dot -Tpng fsm.dot -o test.png. 画图命令



execute : 执行过程

初始化 state , 将inputs 中的每个变量的state状态都置为None (inputs是一个字典)，也就是将每一个输入的变量名字提取出来，将它的状态设为None。返回一个字典集

状态历史设置为（clock, copy.cpoy(state)). Copy.copy 。这种方法复制的list，倘若list中的值发生了变化，拷贝的值也随之发生变化

```
_source_events2events 能够把源时间转化为事件。
```

输入、输出只需要输入name+latency 即可 

源时间，需要输入var,val,lantency. 名字，值，和试验

event代表某个输入，经过某个节点，到达输出状态的过程。