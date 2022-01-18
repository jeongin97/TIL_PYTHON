# 0708
# def 연습
z = 3
def func_1 (a, b):
    y = a + b
    return y

func_1 (2, 3)
print()

# 리스트
lst = list(range(1, 5))
print('lst = ', lst)
lst[0]

lst = [[1, 2, 3, 4], [5, 6, 7, 8]]
lst

# 4까지 더하기
sum = 0
for num in range(5) :
    sum += num
print ("~ 4 =", sum)

# 10까지 더하기
sum = 0
for num in range(11) :              # range(start, end-1, step)
    sum += num
print ("~ 10 =", sum)

# n까지 더하는 함수 만들기_1
def calcsum (n) :
    sum = 0
    for num in range (n + 1):
        sum += num
    return sum

print ("~ 4 = ", calcsum(4))
print ("~ 10 = ", calcsum(10))

# n까지 더하는 함수 만들기_2
def printsum(n) :
    sum = 0
    for num in range(n + 1):
        sum += num
    print ("~", n, "=", sum)

printsum(4)
printsum(10)

#0709
# 실습 1
h = int(input("height : "))
for i in range(1, h+1):
    for j in range(i) :
        print('*', end='')
    print()
def Counter (n) :
    sum = 0
    for num in range(n+1) :
        sum += num
    return sum
print ("star 개수 : ", Counter(h))

# 실습 1 다른 풀이
def star(x) :
    i = 0
    for stage in range(1, x+1) :
        if stage <=x :
            print('*' * stage)
            i += stage
    return i
star_count = star(3)
print("star 개수 : ", star_count)

# 연습
price = 500
print("궁금하면 " + str(price) + "원!")
