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


#8
# 함수명 : print_triangle_withdeco / 매개변수 : 2개 (숫자와 데코문자) / 리턴값 : 없음 / 기능 : 전달된 숫자 개수로 구성되는 삼각형을 출력한다.
# 전달되는 아규먼트 값은 1~10으로 제한한다. 1~10 이외의 값이 전달된 경우에는 처리하지 않는다.
def print_triangle_withdeco (num, deco_code = '%'):
    if 0 < num < 11 :
        i = 0
        for j in range(1, num + 1):
           i += 1
           print(' ' * (10 - i), end='')
           print(deco_code * i)
    else :
        print("1 ~ 10 사이의 숫자가 아닙니다.")
print_triangle_withdeco(3, '*')
print_triangle_withdeco(2, '%')


#9
# 함수명 : sumEven1 / 매개변수 : 가변형 (전달받을 수 있는 아규먼트 개수에 제한이 없다.) / 리턴값 : 1개
# 기능 : 아규먼트는 1 이상의 숫자만 올 수 있으며 전달된 아규먼트들에서 짝수에 해당하는 숫자들만 합을 계산해 리턴한다. 짝수가 없으면 0, 아규먼트가 전달되지 않으면 -1을 리턴한다.
def sumEven1 (*nums):
    even_sum = 0
    if len(nums) >= 1:
        for i in nums:
            if i % 2 == 0:
                even_sum += i
        return even_sum
    else:
        return -1

print(sumEven1())
print(sumEven1(1, 3, 5, 7, 9))
print(sumEven1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


#10
# 함수명 : sumAll / 매개변수 : 가변형 (전달받을 수 있는 아규먼트 개수에 제한이 없다.) / 리턴값 : 1개
# 기능 : 아규먼트가 몇 개가 전달되든 처리하며 호출시 전달되는 아규먼트의 데이터 타입에는 제한이 없다. 전달된 아규먼트 중 숫자타입만 처리하고 숫자가 아닌 데이터는 무시한다. 아규먼트가 전달되지 않았거나 전달되었다 하더라도 숫자가 없으면 None 을 리턴한다.
def sumAll(*nums):
    sum = 0
    for i in nums:
        if type(i) == int:
            sum += i
    if sum == 0:
        return None
    return sum

print(sumAll())
print(sumAll('a', '1'))
print(sumAll('1', '2', 3, 4, 5))
print(sumAll(1.8, 2, '8', 'str', 3))
print(sumAll(1, 2, 3, 4, 5, 6, 7))
print(sumAll(1, 2, 3))


#11
# 함수명 : mydict / 매개변수 : 가변 키워드형 (키=값 형식으로 전달받을 수 있는 아규먼트로 개수에 제한이 없음)
# 기능 : 아규먼트는 '키 = 값' 형식으로 전달되며 아규먼트가 전달되지 않을 시 비어있는 딕셔너리를 리턴한다. 키는 앞에 'my'를 붙인다
def mydict (**kargs) :
    mykargs = {}
    for a, b in kargs.items():
        mykargs["my" + a] = b
    return mykargs


print(mydict(a=2, b=3))
print(mydict(a=2))
print(mydict())


#12
# 함수명 : myprint / 매개변수 : 가변 아규먼트 1개, 가변 키워드 아규먼트 1개 (전달받을 수 있는 아규먼트 개수에 제한이 없다.)
# 기능 : 호출시 전달되는 아규먼트의 데이터 타입에도 제한이 없으며 아규먼트가 전달되지 않으면 "Hello Python"을 출력한다.
def myprint(*args, **kwargs):
    if not args and not kwargs:
        print("Hello Python")
        return

    init_kw = {"deco": "**", "sep": ","}
    init_kw.update(kwargs)

    args_sep = []
    for i in args:
        args_sep.append(str(i))
        args_sep.append(init_kw["sep"])
    args_sep = ''.join(args_sep[:-1])

    print(init_kw["deco"], args_sep, init_kw["deco"], sep="")
myprint(10, 20, 30, deco="@", sep="-")
myprint("python", "javascript", "R", deco="$")
myprint("가", "나", "다")
myprint(100)
myprint(True, 111, False, "abc", deco="&", sep="")

'''
def myprint (*p, deco="**",sep=",") :
    if p is None :
        print("Hello Python")
    else :
        print(deco, end="")
        print(*p, sep=sep, end="")
        print(deco)
'''
'''
ef myprint(*num, **kargs):

  if 'deco' in kargs.keys() and 'sep' in kargs.keys():
    print(kargs['deco'], end='')
    for i in num:
        print(i, end=kargs['sep'])
        for keys, values in kargs.items():
            print(end='')
    print(kargs['deco'])

  elif 'deco' in kargs.keys() and 'sep' not in kargs.keys():
      print(kargs['deco'], end='')
      for i in num:
          print(i, end=',')
          for keys, values in kargs.items():
              print(end='')
      print(kargs['deco'])

  elif 'deco' not in kargs.keys() and len(num) != 0:
      print("**", end='')
      for i in num:
          print(i, end=',')
          for keys, values in kargs.items():
              print(end='')
      print("**")

  elif len(num) == 0 and len(kargs) == 0:
      print("Hello python")
'''
'''
def myprint(*str_tuple, **str_dict):
    if len(str_tuple) == 0:
        print("Hello Python")
        return
    str_list = [n for n in str_tuple]
    str_list[0] = str_dict.get("deco", '**') + str(str_list[0])
    str_list[-1] = str(str_list[-1]) + str_dict.get("deco", '**')
    print(*str_list, sep=str_dict.get("sep", ','))

'''
