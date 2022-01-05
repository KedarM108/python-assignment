import operator
str=input("Enter a string: ")
count={}
for x in str:
    if x in count.keys():
        count[x]+=1
    else:
        count[x]=1
sorted(count.items())

print("The count: ", count)
dsc=dict(sorted(count.items(), key=operator.itemgetter(1), reverse=True))

count=dsc

print("The expected descending order is: ", dsc)



