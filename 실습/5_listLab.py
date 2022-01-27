#1
# 함수를 사용하지 않고 제어문으로 직접 구현하여 리스트 중 최댓값을 추출해 다음과 같이 출력한다.
listnum = [10, 5, 7, 21, 4, 8, 18]
print("최댓값 : ", max(listnum))


#2
# 함수를 사용하지 않고 제어문으로 직접 구현하여 리스트 중 최솟값을 추출해 다음과 같이 출력한다.
listnum = [10, 5, 7, 21, 4, 8, 18]
print("최솟값 : ", min(listnum))


#3
# 함수를 사용하지 않고 제어문으로 직접 구현하여 리스트 중 최댓값, 최솟값을 추출해 다음과 같이 출력한다.
listnum = [10, 5, 7, 21, 4, 8, 18]
print("최솟값 :", min(listnum), ", 최댓값 :", max(listnum), sep="")


#4
# 비어있는 리스트 listnum 을 생성한다. 1~50 사이의 난수를 10개 추출하여 listnum에 추출 순서대로 저장 후 출려간다.
# 리스트의 10보다 작은 값들은 100으로 변경하고 listnum의 모든 값을 출력한다.
import random
listnum = []
for i in range(1, 11) :
    num = random.randint(1, 51)
    listnum.append(num)
print(listnum)

for i in range(len(listnum)) :
    if listnum[i] < 10 :
        listnum[i] = 100
print(listnum[0])       # 인덱싱 방법으로 첫번째 데이터 출력
print(listnum[9])       # 인덱싱 방법으로 마지막 데이터 출력
print(listnum[1:7])    # 슬라이싱 방법으로 두 번째 부터 여섯 번째 출력
print(listnum[::-1])   # 슬라이싱 방법으로 데이터 역순 출력
del listnum[4]          # 인덱싱 방법으로 5번째 데이터 삭제
print(listnum[0:11])    # 슬라이싱 방법으로 데이터 모두 출력
del listnum[1:3]        # 슬라이싱 방법으로 2~3번 데이터 삭제
print(listnum[0:11])    # 슬라이싱 방법으로 listnum의 데이터를 모두 출력한다.


#5
# 비어있는 리스트를 하나 만들어 1~45 사이의 난수 6개를 추출해 중복없이 저장한다.
import random
a = []
while len(a) < 6 :
    num = random.randint(1, 45)
    if num not in a :
        a.append(num)
print("행운의 로또번호 :", end = " ")
for num in range(len(a)-1) :
    print(a[num], end = ", ")
print(a[-1])


#6
a = [
    [10, 12, 14, 16],
    [18, 20, 22, 24],
    [26, 28, 30, 32],
    [34, 36, 38, 40]
]
print("1행 1열의 데이터 :",a[0][0])
print("3행 4열의 데이터 :",a[2][3])
print("행의 갯수 :",len(a))
print("열의 갯수 :",len(a[0]))

print("3행의 데이터들 :", end = "")
for i in a[2] :
    print(i, end=" ")
print()

print("2열의 데이터들 :", end = "")
for i in range(len(a)) :
    print(a[i][1], end=" ")
print()

print("왼쪽 대각선 데이터들 :", end = "")
for i in range(len(a)) :
    print(a[i][i], end=" ")
print()

print("오른쪽 대각선 데이터들 :", end = "")
for i in range(len(a)) :
    print(a[i][len(a)-(i+1)], end=" ")
print()


#7
# 행의 합 구하기
a = [
    [10, 20, 30, 40, 50],
    [5, 10, 15],
    [11, 22, 33, 44]
    [9, 8, 7, 6, 5, 4, 3, 2, 13]
]
for row in range(len(a)) :
    row_sum = 0
    for col in a[row] :
        row_sum += col
    print(row + 1, "행의 합은 ", row_sum, "입니다.", sep="")
    
    
#8
lst = [
    ['B', 'C', 'A', 'A'],
    ['C', 'C', 'B', 'B'],
    ['D', 'A', 'A', 'D']
]
A_sum = 0
B_sum = 0
C_sum = 0
D_sum = 0
for i in range(len(lst)) :
    A_sum += lst[i].count('A')
    B_sum += lst[i].count('B')
    C_sum += lst[i].count('C')
    D_sum += lst[i].count('D')
lst_2 = [A_sum, B_sum, C_sum, D_sum]
print(lst_2)

for i in range(4):
    print(chr(65+i), "는 ", lst_2[i], "개 입니다.", sep="")

''' 8-1
lol = [['B', 'C', 'A', 'A'],
       ['C', 'C', 'B', 'B'],
       ['D', 'A', 'A', 'D']]

countA, countB, countC, countD = 0, 0, 0, 0
for i in range(3):
    for d in lol[i]:
        if d == 'A':
            countA += 1
        elif d == 'B':
            countB += 1
        elif d == 'C':
            countC += 1
        elif d == 'D':
            countD += 1

count = [countA, countB, countC, countD]

for i in range(4):
    print(chr(65+i), "는 ", count[i], "개 입니다.", sep="")
'''
'''8-2
a = [['B','C','A','A'],['C','C','B','B'],['D','A','A','D']]
a1 = 0
a2 = 0
a3 = 0
a4 = 0
for i in range(0,3) :
    for j in range(0,4):
        if a[i][j] == 'A':
            a1 += 1
        elif a[i][j] == 'B':
            a2 += 1
        elif a[i][j] == 'C':
            a3 += 1
        elif a[i][j] == 'D':
            a4 += 1
print('A 는 ',a1,'개 입니다.')
print('A 는 ',a2,'개 입니다.')
print('A 는 ',a3,'개 입니다.')
print('A 는 ',a4,'개 입니다.')
'''
'''8-3
# 1번
list_1 = [['B','C','A','A'],
          ['C','C','B','B'],
          ['D','A','A','D']
          ]

# 3번
A_sum = 0
B_sum = 0
C_sum = 0
D_sum = 0
for i in range(len(list_1)):
    A_sum += list_1[i].count('A')
    B_sum += list_1[i].count('B')
    C_sum += list_1[i].count('C')
    D_sum += list_1[i].count('D')
list_2 = [A_sum,B_sum,C_sum,D_sum]
print(list_2)

# 4번
chr = ['A','B','C','D']
for i in range(4):
    print('{} 는 {}개 입니다.'.format(chr[i],list_2[i]))
'''
''' 8-4
lst = [
    ['B', 'C', 'A', 'A'],
    ['C', 'C', 'B', 'B'],
    ['D', 'A', 'A', 'D']
]


data = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
count_lst = []
for d in data.values(): # for _, d in data.items() :
    count = 0
    for row in lst:
        count += row.count(d)
    count_lst.append(count)

for i, d in data.items():
    print(d, "는 ", count_lst[i], "개 입니다.", sep="")
'''
