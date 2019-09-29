n = int(input())
student_marks = {}
for _ in range(n):
    line = input().split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name] = scores
query_name = input()
a  =  student_marks[query_name]
sum=0
for  i  in  a:
    sum = sum + i
d =  sum/3
print('%.2f'%d)
