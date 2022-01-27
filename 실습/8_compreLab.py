#1
# 
def createList (*args, type=1):
    if len(args) == 0 :
        args = [i for i in range (1, 31)]

    if type == 2 :
        lst = [i for i in args if i % 2 == 0]
    elif type == 3 :
        lst = [i for i in args if i % 2 == 1]
    elif type == 4 :
        lst = [i for i in args if i > 10]
    elif type == 1 :
        lst = [i for i in args]
    return lst

print(createList(2,4,5,12,15,10,24))
print(createList(2,4,5,12,15,10,24,type=2))
print(createList(1,3,5,6,7,11,14,16,17))
print(createList(4,1,2,9,13,34,60,12,8))
print(createList(1,3,6,9,12,15,21))
print(createList(3,6,9,12,15,21))
print(createList(type=4))
print(createList())
