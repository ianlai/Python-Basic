#!/usr/bin/python3
from collections import OrderedDict
from time import time

print("================= List ================= ")
mylist=[]
mylist.append("a")
mylist.append("b")
mylist.append("c")
mylist.insert(2,9)  #add 9 after 2nd element

mylist.append(1)
mylist.append(2)
mylist.pop(0)       #remove element at 0


print(mylist)
print("length:" + str(len(mylist)))


print("================= Dictionary ================= ")
mydict={'aa':10, 'bb':20 , 'cc':30}  #initialize
mydict['n1'] = 111  #add
mydict['n2'] = 222
mydict['n3'] = 333
mydict['n4'] = 444
mydict['n5'] = 0
mydict['n5'] = 555  #update
mydict['n6'] = 666  #add
mydict['a2'] = 222  #add
mydict['a5'] = 555  #add
mydict['a8'] = 222  #add

print("Length of dict: " + str(len(mydict)))
print(mydict)           #arbitrary order 
print(mydict.keys())    #arbitrary order 
print(mydict.values())  #arbitrary order 
print(mydict.items())   #arbitrary order 

##### Find value by key 
targetKey="n5"
print(mydict[targetKey])
print(mydict["n6"])
# print(mydict["n9"])         #search a key not in the dictionary will cause KeyError
print(mydict.get(targetKey))  #use .get(KEY) instead 
print(mydict.get("n9"))       #.get(KEY) will return None if KEY is not in the dictionary

##### Find keys by value (no direct function)
matchKeys=[]
targetValue = 222
for k,v in mydict.items():   # use .items() in python3
    if v == targetValue:
        matchKeys.append(k)
print("Value " + str(targetValue) + " is at  : " + str(matchKeys))

##### Min of key (only when all keys are unorderable, all strings or all integers) 
print("Min key          : " + str(min(mydict)))

##### Min of value (only when all values are unorderable, all strings or all integers) 
print("Min value        : " + str(min(mydict.values())))

##### Key of "Min of value" 
min_value = min(mydict.values())
min_key_list = [k for k,v in mydict.items() if v == min_value]
print("Keys of min value: " + str(min_key_list))


##### Performance of search (linear vs. dictionary)
print(">> Performance comparison ")
idict={}
ilist=[]

starttime0 = time()
# for loop to init
#i=0
#for number in range(1000,10000001):  #1000-100000
#   ilist.append(number)
#   idict[number] = i   
#   i += 1 

# list comprehension and dict comprehension to init
ilist = [i      for i in range(1000,10000001)]
idict = {i:i+10 for i in range(1000,10000001)}
endtime0 = time()

target = 99999

starttime1 = time()
for i,item in enumerate(ilist):
    if item == target:
        print("List got it: " + str(i))
endtime1 = time()

starttime2 = time()
value = idict.get(target)
print("Dict got it: " + str(value))
endtime2 = time()

print("Initialize costs: " + str(endtime0-starttime0))
print("List costs      : " + str(endtime1-starttime1))
print("Dict costs      : " + str(endtime2-starttime2))

print("================= Ordered Dictionary ================= ")
od = OrderedDict()
od["aa"] = 1
od["bb"] = 2
if "bb" in od: od["bb"] += 1
print(od)

for i in od:
    print(i , od[i])
