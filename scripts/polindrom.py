n=int(input('n='))
p=n
m=0
while p!=0:
    a=p%10
    p=p//10
    m=m*10+a
if n==m:
    print('поліндром')
else:
    print('не поліндром')
