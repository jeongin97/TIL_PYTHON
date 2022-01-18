# 1
# 함수명 : print_book_title / 매개변수와 리턴값 없음 / 기능 : 파이썬 교재명을 화면에 출력한다.
# 함수명 : print_book_publisher / 매개변수와 리턴값 없음 / 기능 : 파이썬 교재의 출판사명을 화면에 출력한다.
def print_book_title ():
    print("파이썬 정복")
    return

def print_book_publisher ():
    print("한빛미디어")
    return

for _ in range(3) :
    print_book_title()
for _ in range(5) :
    print_book_publisher()
    
   
# 2
# 함수명 : get_book_title / 매개변수 : 없음 /리턴값 : 있음 / 기능 : 파이썬 교재명을 리턴한다.
# 함수명 : print_book_publisher / 매개변수 : 없음 /리턴값 : 있음 / 기능 : 파이썬 교재의 출판사명을 리턴한다.
# get_book_title() 함수를 호출하고 리턴되는 결과를 name 변수에 저장한 후 name 변수의 값을 2회 출력한다.
# get_book_publisher() 함수를 호출하고 리턴되는 결과를 화면에 출력한다.
def get_book_title ():
    return "파이썬 정복"
  
def get_book_publisher ():
    return "한빛미디어"

name = get_book_title()

for _ in range(2) :
    print(name)
    
print(get_book_publisher())


# 3
# 함수명 : expr / 매개변수 : 숫자 2개와 연산자 1개 /리턴값 : 연산 결과 또는 None
# 기능 : 전달된 두 개의 숫자에 대해서 전달된 연산을 처리하고 그 결과를 리턴한다.
# 연산자는 +,-,*,/ 만 처리하며 그 외의 연산자는 연산을 하지 않고 None을 리턴한다.
# 숫자 2개와 연산자 1개를 전달하여 expr() 이라는 함수를 호출한 다음 리턴 결과가 None 이면 수행불가를 출력하고 그렇지 않으면 연산결과 : XX 를 출력한다.
def expr (num1, num2, z) :
    if z == '+' :
        return num1 + num2
    elif z == '-' :
        return num1 - num2
    elif z == '*' :
        return num1 * num2
    elif z == '/' :
        return num1 / num2
    else :
        return None

final = expr(7, 2, '+')
if final == None :
    print("수행 불가")
else :
    print("연산결과 :", final, sep="")


#4
# 함수명 : print_triangle / 매개변수 : 1개 / 리턴값 : 없음 / 기능 : 전달된 숫자 개수로 구성되는 삼격형을 출력한다. (1~10 사이만)
def print_triangle (x) :
    if (x < 1) or (x > 10) :
        return

    for i in range(1, x+1, 1) :
        for _ in range(i) :
            print('*', end="")
        print()

    return

print_triangle(3)
print_triangle(0)
print_triangle(7)


#5
# 함수명 : print_triangle / 매개변수 : 1개 / 리턴값 : 없음 / 기능 : 전달된 숫자 개수로 구성되는 역삼격형을 출력한다. (1~10 사이만)
def print_triangle (x) :
    if (x < 1) or (x > 10) :
        return

    for i in range(x, 0, -1) :
        for _ in range(i) :
            print('*', end="")
        print()

    return

print_triangle(2)
print_triangle(5)
print_triangle(8)


#6
# 함수명 : print_gugudan / 매개변수 : 1개 / 리턴값 : 없음 / 기능 : 전달된 숫자의 구구단 출력.
# (int 타입 아니면 그냥 리턴, 1~9사이만 출력, 그 외의 경우 해당 단의 구구단을 행 단위로 출력)
def print_gugudan (x) :
    if type(x) != int :
        return
    elif (x < 1) or (x > 9) :
        return
    else :
        for i in range(1, 10) :
            print(x,"x",i,"=",x*i)
        return

print_gugudan(7)
print_gugudan(3)


#7
# 함수명 : differtwovalue / 매개변수 : 2개 / 리턴값 : 연산 결과 / 기능 : 전달된 2개의 데이터 중, 큰 값에서 작은 값의 차를 리턴, 두 값이 동일하면 0리턴
# 1부터 30 사이의 난수 2개 추출하여 2번 구현된 함수를 호출하고 결과를 "X와 Y의 차는 W 입니다." 형식으로 출력
import random

def diffetwovalue (x, y) :
    if x != y :
        return abs(x-y)
    else :
        return 0

for _ in range(5) :
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    print(num1,"와", num2, "의 차는", diffetwovalue(num1, num2), "입니다.")

'''
import random

def differtwovalue(i, j):
    if i > j:
        k = i - j
        return k
    elif i < j:
        k = j - i
        return k
    else:
        return 0


for i in range(5):
    j = random.randint(1, 30)
    k = random.randint(1, 30)
    print(j, '와', k, '의 차는', differtwovalue(j, k), '입니다.')
'''


