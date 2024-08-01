a, b = map(int, input().strip().split(' '))
temp = ''
for i in range(0,b):
    for j in range(0,a):
        temp+='*'
    temp+='\n'
print(temp)