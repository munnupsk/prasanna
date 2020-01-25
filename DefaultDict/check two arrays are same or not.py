#https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not/0/?track=md-hashing&batchId=144

from collections import defaultdict
for _ in range(int(input())):
    l=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    flag=1
    h=defaultdict(lambda:0)
    for i in l1:
        h[i]+=1
    
    for i in l2:
        if i not in h:
            flag=0
            print('0')
            break
        if i in h and h[i]!=0:
            h[i]-=1
    if flag :
        print('1')
