data  =  []
sc  =  []
for j in range(int(input())):
    name = input()
    score = float(input())
    sc+=[score]
    data+=[[name,score]]
sc1  =[]
for  i  in  sc:
    if  i not  in  sc1:
        sc1+=[i]
sc1.sort()
a  =  sc1[1]
name=[]
for  i  in  data:
    if  i[1]  ==  a:
        name+=[i[0]]
name.sort()
for  i  in  name:
    print  (i)