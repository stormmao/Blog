from collections import deque
graph = {}
graph["you"] = ["alice","bob","claire"]#散列表的创建
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj","peggy"]
graph["claire"] = ["thom","jonny"]
graph["peggy"] = []
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = ["tom"]
def person_is_seller(name):#寻找的标准
    return name[-1] == 'm'
def search(name):
    search_queue = deque()#创建待搜索的队列
    search_queue += graph[name]#传入初始参数
    searched = []#记录已经搜索过得节点，防止无限循环
    while search_queue:#待搜索队列不空就搜索
        person = search_queue.popleft()#弹出队头的数据进行判断
        if not person in searched:
            if person_is_seller(person):
                print(person)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False#队列空了，程序结束
search("you")

