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

   
    
    
