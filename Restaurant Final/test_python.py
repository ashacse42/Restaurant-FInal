n=int(input())
#n=input()
print(n)
list=[]
for i in range(0,n):
    list.append(i)
print(list)

for i in list:
    if str(i)=='3':
        print(i)
    #print(i)

list.clear()
print(list)

number=dict()
number['a']=85
number['b']=85
print(number.keys())
print(number.values())
print("c" in number)

number['c']=[12,15]
print(number)
string="abra"
print(string.find('a'))




