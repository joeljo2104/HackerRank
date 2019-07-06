n = int(input())
arr = map(int, input().split())
arr1=[]
for  i  in  arr: 
    if  i  not  in  arr1:
        arr1+=[i]
arr1.sort()
print (arr1[-2])
