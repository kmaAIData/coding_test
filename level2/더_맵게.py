# -*- coding: utf-8 -*-
"""더 맵게.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/129VmGJVZuHvOqGntWaNfnC_L5R8mEbcx
"""

def solution(scoville, K):
    count=0
    for i in range(len(scoville)-1):
        scoville=sorted(scoville)
        if scoville[0]<K:
            if i == (len(scoville)-2):
                count=-1
            else:
                scoville.append(scoville[0]+scoville[1]*2)
                del scoville[0:2]
                count+=1
        else: 
            break
    answer = count
    return answer
