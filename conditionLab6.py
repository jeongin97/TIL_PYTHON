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