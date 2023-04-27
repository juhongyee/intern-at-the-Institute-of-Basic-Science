#baum-welch algorithm
import numpy as np

# matrix의 크기 입력
m = int(input("matrix의 크기를 입력하세요"))
#유니폼 분포 확률
p_uni = 1/m

#A를 uniform 분포로 선언
A = [[p for i in range(m)] for i in range(m)]

A = np.array(A)

#B를 선언, 각 학습수준에 맞게 확인할 확률 0.9로 시작




