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


