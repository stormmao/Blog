processed = []#记录所有已处理的节点

graph = {}#整个图的设置
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 2
graph["b"] = {}
graph["b"]["fin"] = 5
graph["b"]["a"] = 3
graph["fin"] = {}

infinity = float("inf")#无限大，用作参考点
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None #与37行的条件判断相呼应

def find_lowest_cost_node(costs):#找出花销最少的节点
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return  lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:  #运行到最后会是None，因为所有节点已处理，如27行的初始赋值所示
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] >new_cost:#判断大小，更新开销
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)#处理过的节点写入数组
    node = find_lowest_cost_node(costs)#处理剩下的节点
print(parents)
print(costs)