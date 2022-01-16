# [실습 1]
# for 문을 활용하여 '1 2 3 4 5 6 7 8 9 10' 출력하도록 구현, print()로 숫자 1개씩 출력하게 할 것.
for i in range(1, 11, 1) :
    print(i , end = " ")
    
    
# [실습 2]
# 0부터 5까지 하나씩 개행해서 출력하도록 구현, print() 함수로 숫자 하나만 출력
for i in range(0, 5, 1) :
    print (i)


# [실습 3]
# '@' 기호 문자가 하나씩  개행하여 출력되도록 구현, print() 함수 호출을 5번 반복하게 한다.
for _ in range(5):
    print("@")


# [실습 4]
# 9부터 4까지 '9 : 홀수' 와 같은 형식의 결과가 개행하여 출력되도록 구현.
for i in range(9, 3, -1) :
    if i % 2 == 0 :
        print ("%d : 짝수" % i)
    else :
        print ("%d : 홀수" %i)


# [실습 5]
# 1부터 10 사이의 난수를 추출하여 start 변수에 저장하고 30부터 40 사이의 난수를 추출하여 end 변수에 저장한다.
# start 부터 end 까지의 숫자들 중에 짝수의 합을 구해 'X부터 Y 까지의 짝수의 합 : ZZ' 형식으로 출력한다.
import random
start = random.randint(1, 10)
end = random.randint(30,40)

"""
evensum
for i in range (start) :
    if i % 2 == 0 :
        evenisum += i
    print (evenisum)
for j in range (end) :
    if j % 2 == 0 :
        evenjsum +=j
    print(evenjsum)

evensum = evenisum + evenjsum
print ("X 부터 Y 까지의 짝수의 합 : " , evensum)
"""

evenSum = 0
for i in range(start, end+1, 1):
    if i % 2 == 0:
        evenSum = evenSum+i
print(start, '부터', end, '까지의 짝수의 합 :', evenSum)


# [실습 6]
# evenNum 변수와 oddNum 변수의 값을 0으로 대입한 후 1부터 100까지의 값 중에서 짝수의 합은 evenNum에 누적하고 홀수의 합은 oddNum에 누적한다.
# '1부터 100까지의 숫자들 중에서 \n 짝수의 합은 XXX 이고 \n 홀수의 합은 YYY 이다.' 라고 출력한다.
evenNum = 0
oddNum = 0
for i in range(1, 101, 1) :
    if i % 2 == 0 :
        evenNum += i
    else :
        oddNum += i
print("1부터 100까지의 숫자들 중에서 \n"
      "짝수의 합은 ", evenNum, " 이고 \n"
                          "홀수의 합은 ", oddNum, " 이다." )
