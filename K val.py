import bisect
case= list(map(int,input().split())) # create a list of Integer from a list of String
N=case[0] #5
M=case[1] #3
k=case[2] #2
numbers=list(map(int,input().split()))

numbers.extend(numbers[:M-1])

begin=numbers[0:M]
begin.sort()
kVals=[]
kVals.append(begin[k-1])
#print(forIter)
for i in range(N-1):
    to_be_removed=numbers[i]
    to_be_added=numbers[i+M]

    remove_index_in_sorted=bisect.bisect(begin,to_be_removed)-1 # removing index in begin
    del begin[remove_index_in_sorted] # delete index in sorted array
    bisect.insort_left( begin, to_be_added) # insert New value to the sorted arry
    kVals.append(begin[k-1])



kVals.sort()
print(kVals[0])