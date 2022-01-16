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
