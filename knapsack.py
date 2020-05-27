#tkaing values
n,W =  [int(x) for x in input().split()]

#checking max_limits of knapsack
if W==0:
    print(0)
    quit()

#getting values of value and weight of each item
lst = []
for i in range(n):
    v,w = [int(j) for j in input().split()]
    if v==0:
        continue
    lst.append((v,w))


#sorting the lst with respect to v/w value
lst.sort(key = lambda x: x[0]/x[1] , reverse=True)

total_value = 0


for v,w in lst:
    if W==0:  #checking if the limit has reached
        #print(total_value)
        quit()
    amt = min(w,W)               #taking the minimum of W, i.e Total weight and w,which represent weight of object
    total_value+=amt*v/w         # adding the value to the list///
    W-=amt                       #subtracting the amount !

print(total_value)

