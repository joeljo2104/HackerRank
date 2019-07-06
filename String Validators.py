a,b,c,d,e=0,0,0,0,0
s = input()
for i in s:
    if i.isalnum():
        a=1
    if i.isalpha():
        b=1
    if i.isdigit():
        c=1
    if i.islower():
        d=1
    if i.isupper():
        e=1
if a==1:
    print(True)
else:
    print(False)
if b==1:
    print(True)
else:
    print(False)
if c==1:
    print(True)
else:
    print(False)
if d==1:
    print(True)
else:
    print(False)
if e==1:
    print(True)
else:
    print(False)
