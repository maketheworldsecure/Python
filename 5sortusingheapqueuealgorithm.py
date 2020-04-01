#! usr/bin/env python

import heapq as dk
Getnumbers =[2,5,1,6,7,1,9]
s_result=[]
print("Input Numbers:")
print(Getnumbers)
dk.heapify(Getnumbers)
print("\nSorted Numbers:")
for i in range(len(Getnumbers)):
	sort_result.insert(i,dk.heappop(Getnumbers)) 
print(sort_result)



