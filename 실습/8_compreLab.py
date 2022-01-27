#1
# 함수명 : createList / 매개변수 : 0개 이상의 위치 아규먼트를 받는 매개변수 1개 --> 가변인수, 기본값이 있는 매개변수 1개(매개변수 명은 type=1)
# 기능 : 0개 이상의 위치 아규먼트를 가지고 리턴. 아규먼트가 전달되지 않을 경우 1부터 30까지의 값으로 type에 따른 리스트를 생성, 리턴한다.
# type=2, 짝수에 해당하는 데이터들로 리스트 생성/ type=3, 홀수에 해당하는 데이터들로 리스트 생성/ type=4, 10보다 큰 데이터들로 리스트 생성/ 
# type=1, 데이터 값 모두를 가지고 리스트 생성
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


#2
# 함수명 : mycompredict / 매개변수 : 가변 키워드형(0개 이상의 '키=값' 형식의 아규먼트를 받아 처리한다.)
# 기능 : funcLab의 11번 mydict()라는 함수의 기능과 동일하게 구현하는데 이번에는 딕셔너리 컴프리핸션 구문을 사용해 생성한다.
def mycompredict (**kargs):
    mykargs = {"my" + k : v for k, v in kargs.items()}
    return mykargs
print(mycompredict(a=2, b=3))
print(mycompredict(a=2))
print(mycompredict())
