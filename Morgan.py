case = list(map(int,input().split()))
subjects=case[0]
num_of_constraints=case[1]

constraints=[]
for x in range(num_of_constraints): # get constraints and put them in a list
    constraints.append(list(map(int,input().split())))

unique=set(constraints[0]) # take 1st record and put them in set

for recrd in constraints[1:]: #create a list of all unique numbers in constraints
    unique |=set(recrd)
plan = list(map(int,input().split()))

state=True
if(not (len(unique) == len(plan))): # if the subjects are differ than given constraints
    state=False

for x in constraints:
    if plan.index(x[0])>plan.index(x[1]):
        state=False

out="YES" if state else "NO"
print(out)