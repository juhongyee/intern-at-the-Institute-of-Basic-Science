from collections import defaultdict
import pandas as pd
import math
import time

forest = defaultdict(int) #root node of each tree {Node.item : Node}
schedule = [] #optimal learning strategy = Result
N = 60 #num of entire node
nodelist = [0 for i in range(N)] #list of nodes

class Node:
    def __init__(self, item, c):
        self.item = item #node 번호
        self.c = c
        self.mu = item
        self.rho = None #sum(c)/sum(mu)
        self.child = [] #List of child nodes
        self.root = None #root node
        self.path = [] #from root node to current node

def init():
    path = "/Users/seongeunkim/Desktop/Workspace/학부인턴/Algorithm/tree_structure_data.csv"
    df = pd.read_csv(path)

    global N
    for i in range(0, N):
        #print("i : ", i)
        row = df.loc[i]
        #print("row : " ,row)
        item = row[0]
        pred = row[1]
        c = row[2]
        mu = row[3].split(":")
        mu_int = int(mu[0])*3600 + int(mu[1])*60 + int(mu[2])
        if (i == 0):
            #root node
            nodelist[0] = Node(item, c)
            nodelist[0].root = nodelist[0]
            nodelist[0].mu = mu_int
            forest[str(nodelist[0].item)] = nodelist[0]
            #print("root:",nodelist[0])
            continue
        nodelist[i] = Node(item, c)
        #print("node : ",nodelist[i])
        nodelist[i].mu = mu_int
        nodelist[i].root = nodelist[0]
        pred_node = nodelist[pred - 1]
        pred_node.child.append(nodelist[i])


maxRho = 0
maxRhoNode = None
def findMaxRho(node, sum_c, sum_mu, path):
    global maxRho
    global maxRhoNode

    sum_c += node.c
    sum_mu += node.mu
    node.rho = sum_c/sum_mu

    node.path = path.copy()
    node.path.append(node.item)

    if(node.rho >= maxRho):
        maxRho = node.rho
        maxRhoNode = node
    if(len(node.child) > 0):
        for n in node.child:
            findMaxRho(n, sum_c, sum_mu, node.path)

def appendElements(A, B):
    for i in B:
        A.append(i)
    return A

def setRoot(node, root):
    node.root = root
    if(len(node.child) > 0):
        for n in node.child:
            setRoot(n, root)
    else:
        node.root = root
        return

def makeRoot(node):
    forest[str(node.item)] = node
    setRoot(node, node)

def makeForest(node, path):
    global i
    if(node.item == path[i]):
        i += 1
        if(i + 1 == len(path)): #마지막 노드까지 옴.
            if(len(node.child) > 0):
                for n in node.child:
                    makeRoot(n)
            return
        else:
            for n in node.child:
                makeForest(n, path)
    else:
        makeRoot(node)
        return

#Main
start = time.time()
init()
while(len(schedule) < N):
    maxRho = 0
    maxRhoNode = None
    for t in forest:
        sum_c = 0
        sum_mu = 0
        path = []
        findMaxRho(forest[t], sum_c, sum_mu, path)
    schedule = appendElements(schedule, maxRhoNode.path)
    path = maxRhoNode.path.append(-1)
    del(forest[str(maxRhoNode.root.item)])
    i = 0
    makeForest(maxRhoNode.root, maxRhoNode.path)

end = time.time()

print("schedule : ", schedule)

#print(f"{end-start:.5f} sec") #0.03237 sec

# schedule :  [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 
#              18, 24, 25, 27, 28, 29, 30, 26, 31, 34, 
#              35, 32, 33, 9, 8, 36, 37, 38, 39, 42, 
#              43, 44, 40, 41, 49, 45, 6, 7, 46, 47, 
#              48, 15, 16, 50, 51, 17, 19, 23, 20, 21, 
#              22, 52, 53, 54, 55, 56, 57, 58, 59, 60]
