import sys
input = sys.stdin.readline

age = []
sex = []
first_age, first_sex = list(map(str,input().split()))
second_age, second_sex = list(map(str,input().split()))
age.append(int(first_age))
age.append(int(second_age))
sex.append(first_sex)
sex.append(second_sex)
IsMale = False
for i in range(2):
    if int(age[i] )>=19 and sex[i] == 'M':
        IsMale = True
        break

print(1 if IsMale else 0)