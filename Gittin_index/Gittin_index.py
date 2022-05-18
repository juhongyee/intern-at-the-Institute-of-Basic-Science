import numpy as np
import sys
from collections import deque
import math

#initialize
def init():
    #state space 입력
    print("state space 입력")
    X = list(map(int,sys.stdin.readline().split()))
    
    global length
    length = len(X)
    #transition matrix 입력
    print("transition matrix 입력")
    
    #zero matrix 선언
    trans_M = np.zeros((length,length),dtype=np.float64)
    
    #probability 입력
    for i in range(0,length):
        line = list(map(float,sys.stdin.readline().split()))
        for j in range(0,length):
            trans_M[i][j] = line[j]
    
    #reward vector 선언
    reward = deque()
    
    #reward 입력
    print("reward vector 입력(정수)")
    line = list(map(int,sys.stdin.readline().split()))
    for i in range(length-1,-1,-1):
        reward.appendleft(line[i])

    #max_value of reward
    maximum = max(reward)
    
    #argmax
    for i in range(0,len(reward)):
        if(reward[i] == maximum):
            maximum = i+1
            break
        
    #𝛃 값 입력
    print("베타 값 입력")
    B = float(input())
    return (trans_M,reward,maximum,X,B)

def recursive_part(trans_M,reward,C,S,X,B,gittin):
    Q_k = np.zeros((length,length))
    
    for i in C:
        col = trans_M[:,(i-1)]
        for j in range(0,length):
            Q_k[j][i-1] = col[j]
    
    identity = np.eye(length,length)
    
    #d_k
    d_k = (np.linalg.inv(identity-B*Q_k))@reward
    
    #b_k
    one = 1+np.zeros(length)
    b_k = (np.linalg.inv(identity-B*Q_k))@one
    
    #d_k/b_k
    arg_choose = d_k/b_k
    
    #d_k/b_k의 max value finding
    max_index = 0
    max  = -math.inf
    for i in S:
        if(max<arg_choose[i-1]):
            max_index = i
            max = arg_choose[i-1]
            
    #𝛂_k선택
    C.appendleft(max_index)
    if(S):
        S.remove(max_index)
    gittin[max_index-1] = max
    
temp = init()

trans_M = temp[0]
reward = temp[1]
a1 = temp[2]
X = temp[3]
B = temp[4]

#gittin index 저장
gittin = [0 for i in range(length)]
gittin[a1-1] = reward[a1-1]

#continuous and stopping
C = deque()
C.appendleft(a1)
S = deque()

#deep copy
for i in range(len(X)-1,-1,-1):
    S.appendleft(X[i])
S.remove(a1)

for i in range(length-1):
    recursive_part(trans_M,reward,C,S,X,B,gittin)

print(gittin)







