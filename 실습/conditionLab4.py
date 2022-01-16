# [실습 4]
import random
grade = random.randint(1, 6)

print("grade(", grade, ") : ", sep="")
if grade == 1 or grade == 2 or grade == 3 :
    print (grade, "학년은 저학년입니다.")
else :
    print (grade, "학년은 고학년입니다.")
