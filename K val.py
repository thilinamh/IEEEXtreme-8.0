import bisect
case= list(map(int,input().split()))
N=case[0] #5
M=case[1] #3
k=case[2] #2
ls=input().strip().split()
numbers=list(map(int,ls))

forIter=numbers
forIter.extend(numbers[:M-1])


begin=forIter[0:M]
begin.sort()
kVals=[]
kVals.append(begin[k-1])
#print(forIter)
for i in range(N-1):
    to_be_removed=forIter[i]
    to_be_added=forIter[i+M]
    #print(i+M-1)
   # print("to be added",to_be_added )

    remove_index_in_sorted=bisect.bisect(begin,to_be_removed)-1 # removing index in begin
    del begin[remove_index_in_sorted] # delete index in sorted array
    bisect.insort_left( begin, to_be_added) # insert New value to the sorted arry
    kVals.append(begin[k-1])
#print(subsets)



kVals.sort()
#print(kVals)
print(kVals[0])