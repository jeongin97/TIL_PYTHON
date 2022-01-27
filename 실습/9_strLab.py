#1
# 함수명 : myemail_info / 매개변수 : 이메일 주소 문자열 1개 / 리턴값 : 2개의 원소를 갖는 튜플
# 기능 : 전달된 이메일 주소 문자열에서 @ 를 기준으로 쪼개서 튜플을 만들어 리턴하며 문자열에 @가 없으면 None을 리턴한다.
def myemail_info (email):
    s = email
    if '@' in s:
        s2 = s.split('@')
        tu = tuple(s2)
        print(tu)
    else:
        print("none")
myemail_info('dbswjddls97@naver.com')
myemail_info('vdssnaver.com')


#2
#s1 문자열의 기링 출력
s1 = "pythonjavascript"
print(len(s1))

# s2에서 '-'를 빼고 출력한다.
s2 = "010-7777-9999"
print(s2.replace("-",""))

#s3 문자열을 반대로 출력
s3 = "PYTHON"
print(s3[::-1])

#s4 문자열을 소문자로 출력
s4 = "Python"
print(s4.lower())

#s5 문자열에서 www.python.org만 뽑아서 출력
s5 = "https://www.python.org/"
print(s5.lstrip("htps:/").rstrip('"').rstrip('/'))

#주민등록 번호에서 7자리 숫자를 사용해 남성, 여성을 판별한다.
s6 = '891022-2473837'
s6_1 = s6.split("-")
s6_2 = s6_1[1]
if s6_2[0] =='1'  or  s6_2[0] == '3' :
    s6_sex = "남성"
if s6_2[0] =='2'  or  s6_2[0] == '4' :
    s6_sex = "여성"
print(s6_sex)

#s7값을 정수형 숫자, 실수형 숫자로 변환해 출력
s7 = '100'
print(int(s7))
print(float(100))

#s8 문자열에서 'n' 문자가 몇개인지 출력한다.
s8 = 'The Zen of Python'
print(s8.count('n'))

#s8에서 'Z'의 위치 출력
print(s8.find('Z'))

#s8에서 모두 대문자로 변환한 후 공백단위로 분리해 리스트로 만들어 출력
s8_2 = s8.upper()
print(s8_2.split(" "))
