#this is a comment {^-^}
x=3
y=4
MyName="Cyber.33"
print("this is python in 10 minutes")
print(x)
print(MyName)

def sumation(a,b):
    print("funtion is called")
    return a+b

sumation(x,10)
print(sumation(x,10))
print(sumation('hello ',MyName))

MyList=[5,5,4,3,2,1,'b','b','a']
print(MyList)
print(len(MyList))
print(MyList[0], MyList[8])
MyList[0]='33'
MyList.append("3333")
print(MyList)

MySet={5,5,4,3,2,1,'b','b','a'}
print(MySet)
print(len(MySet))
MySet.add("333")
print(MySet)

MyTuple=(5,5,4,3,2,1,'b','b','a')
print(MyTuple)
print(len(MyTuple))
print(MyTuple[0], MyTuple[8])

MyDict1={'name':'jack', 'age':23}
MyDict2={'name':'lora', 'age':18}
print(MyDict1.keys())
print(MyDict1.values())
print(MyDict1['name'])
people=[MyDict1,MyDict2]
print(people[1]['age'])

x=-5
y=-6
z=7
print(x>0)
print(x<0)
if(x>0):print("positive")
else:print("negative")

if(x<0 and y<0):print("both negative")

if(x<0 or z<0):print("at least one of them is negative")
else:print("both positive")

if((z==0)):print("z is equal to zero")

if(x<0 and y<0 and z<0):print("all negative")
elif(x>0 and y>0 and z>0):print("all positive")
else:print("they are different")

even=[2,4,6,8]
MyName="cyber.33"

for i in even:
    print(i, " is even number")

for i in MyName:
    print(i)

j=0
while j<5:
    print(j," is less than 5")
    j+=1

import pandas as pd
MyList=[2,3,4]
print(pd.Series(MyList).product())
