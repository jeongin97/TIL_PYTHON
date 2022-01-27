#1
import random
s1 = set()
s2 = set()
for _ in range(10):
    s1.add(random.randint(1, 20))
    s2.add(random.randint(1, 20))

# 1-1
print("집합1: ", s1)
print("집합2: ", s2)
# 1-2 : 교집합
print("두 집합에 모두 있는 데이터: ", s1 & s2)
# 1-3 : 합집합
print("집합1 또는 집합2에 있는 데이터: ", s1 | s2)
# 1-4 : 차집합
print("집합1에는 있고 집합2에는 없는 데이터: ", s1 - s2)
print("집합2에는 있고 집합1에는 없는 데이터: ", s2 - s1)
# 1-5 : 대칭차집합
print("집합1과 집합2가 각자 가지고 있는 데이터: ", s1 ^ s2)

'''
rom random import randint


num_set1, num_set2 = set(), set()
while len(num_set1) < 10:
    num_set1.add(randint(1, 20))
while len(num_set2) < 10:
    num_set2.add(randint(1, 20))
'''


#2
# 행운의 로또번호  : X, X, X, X, X, X
import random
luck = set()
while len(luck) < 6:
    luck.add(random.randint(1, 45))

print('행운의 로또번호 :',end=' ')
a = list(luck)
for i in range(len(a)-1):
    print(a[i],end=',')
print(a[-1])
