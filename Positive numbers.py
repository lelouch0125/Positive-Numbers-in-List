#Printimg positive numbers in list

#list=[]
#l2=[]
#print("Enter elements")
"""for i in range(0,n):
    a=int(input())
    list.append(a)"""



l1=list(map(int,input("Enter elements\n").strip().split()))
l2=[]
for j in l1:
    if j>0:
        l2.append(j)
print(l2)
