# [실습 1]
num = int(input("숫자를 입력하세요 : "))
if num > 10 :
    print("OK")
''''''
input_data = input("숫자를 입력하세요 : ")
num = int(input_data)
if num > 10 :
    print("OK")
''''''


# [실습 2]
color_name = input("color_name 을 입력하세요 :")
if color_name == "red" :
    print("'#ffOOOO'")
if color_name != "red" :
    print("'#OOOOOO'")
    
    
# [실습 3]
import random
grade = random.randint(1, 6)
if grade >= 1 and grade < 4 :
    print (grade, "학년은 저학년입니다.")
else :
    print (grade, "학년은 고학년입니다.")

    
# [실습 4]
import random
grade = random.randint(1, 6)
print("grade(", grade, ") : ", sep="")

if grade == 1 or grade == 2 or grade == 3 :
    print (grade, "학년은 저학년입니다.")
else :
    print (grade, "학년은 고학년입니다.")   
    
    
# [실습 5]
import random
score = random.randint(0, 100)

if score >= 90 and score <= 100 :
    print (score, "점은 A등급입니다.", sep="")
if score >= 80 and score <= 89 :
    print (score, "점은 B등급입니다.", sep="")
if score >= 70 and score <= 79:
    print(score, "점은 C등급입니다.", sep="")
if score >= 60 and score <= 69 :
    print (score, "점은 D등급입니다.", sep="")
else :
    print (score, "점은 F등급입니다.", sep="")
    
''''''
import random
score = random.randint(0, 100)

if score >= 90 and score <= 100:
    print(score, "점은 A등급입니다.", sep="")
elif score >= 80 and score <= 89:
    print(score, "점은 B등급입니다.", sep="")
elif score >= 70 and score <= 79:
    print(score, "점은 C등급입니다.", sep="")
elif score >= 60 and score <= 69:
    print(score, "점은 D등급입니다.", sep="")
else:
    print(score, "점은 F등급입니다.", sep="")
''''''


# [실습 6]
import random
score = random.randint(0, 100)

if score >= 60 and score <= 100 :
    level = "D"
    if score >= 70 and score <= 79 :
        level = "C"
    if score >= 80 and score <= 89:
        level = "B"
    if score >= 90 and score <= 100 :
        level = "A"
else :
    level = "F"
print (score, "점은 ",level,"등급입니다.", sep="")

''''''
if score >=90 :
    grade = "A"
elif score>=80 :
    grade = "B"
elif score>=70 :
    grade = "C"
elif score>=60 :
    grade = "D"
else :
    grade = "F"
print (score, "점은 ",grade,"등급입니다.", sep="")
''''''


# [실습 7]
num = int(input("1부터 10사이의 숫자를 하나 입력하세요 :"))
if 1 <= num <= 10 :
    if num % 2 == 1 :
        print(num, ": 홀수")
    else :
        print(num, ": 짝수")
else :
    print("1부터 10사이의 값이 아닙니다.")
    
    
# [실습 8]
import random
over_num = random.randint(1, 10)
if over_num == 1 or over_num == 6 :
    k = 300+50
if over_num == 2 or over_num == 7 :
    k = 300-50
if over_num == 3 or over_num == 8 :
    k = 300*50
if over_num == 4 or over_num == 9 :
    k = 300/50
if over_num == 5 or over_num == 10 :
    k = 300%50
print ("결과값 :",k,sep = "")

''''''
import random
over_num = random.randint(1, 10)
if over_num == 1 or over_num == 6 :
    k = 300+50
elif over_num == 2 or over_num == 7 :
    k = 300-50
elif over_num == 3 or over_num == 8 :
    k = 300*50
elif over_num == 4 or over_num == 9 :
    k = 300/50
else :
    k = 300%50
print ("결과값 :",k,sep = "")
''''''
