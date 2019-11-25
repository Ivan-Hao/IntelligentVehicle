import sys
time = 0
back_edge = []
class vertex():

    def __init__(self, args):
        self.number = args
        self.edge = []
        self.ischeck = 'white'
        self.checktime = 0
        self.endtime = 0
        self.predecessor = None

    def add_connect(self, args):
        self.edge.append(args)

def dfs(vertex,vertex_list,predecessor=None):
    global time 
    global back_edge
    time += 1
    vertex.checktime = time
    vertex.ischeck = 'gray'

    for j in vertex.edge :
        if j in vertex_list.keys() and vertex_list[j].ischeck == 'white':
            vertex_list[j].predecessor = vertex 
            dfs(vertex_list[j],vertex_list,vertex)
        elif j in vertex_list.keys() and vertex_list[j].ischeck == 'gray':
            back_edge.append(dict(front = vertex.number, end = vertex_list[j].number))

    vertex.ischeck = 'black'
    time +=1
    vertex.endtime =time

if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    input_file = open(sys.argv[1],'r')
    total_amount = int(input_file.readline())
    total_edge = int(input_file.readline())
    vertex_list = {}
    
    for edge in input_file.readlines():
        vertex_front,vertex_rear = edge.strip().split()
    
        if vertex_front not in vertex_list.keys():            
            temp = vertex(vertex_front)
            temp.add_connect(vertex_rear)
            vertex_list[vertex_front]=temp
        else:
            vertex_list[vertex_front].add_connect(vertex_rear)

    input_file.close()

    for i in vertex_list.keys():
        if vertex_list[i].ischeck == 'white' : 
            dfs(vertex_list[i],vertex_list)
    if back_edge == []:
        print("There is no cycle in graph!")
    else:
        print("There is a cycle in graph!")
        for j in back_edge:
            print("The removal edge",j)
    
        