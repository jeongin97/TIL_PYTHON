#1
# 칼라와 칼라의 RGB 값을 찾아 딕셔너리를 생성, 사용자에게 칼라명을 입력받아 RGB 값 출력하기
col_dic = {
    'red' : '#ff0000', 'blue' : '#0000ff',
    'green' : '#008000', 'yellow' : '#ffff00',
    'orange' : '#ffa500', 'black' : '#000000',
    'white' : '#ffffff', 'violet' : '#ee82ee',
    'pink' : '#ffc0cb', 'lime' : '#00ff00'
}

col= str(input("칼라명을 영문으로 입력하세요 :"))
if col in col_dic :
    print(col,"칼라의 RGB 값은",col_dic[col],"입니다")
else :
    print(col,"칼라의 RGB 값을 찾을 수 없습니다.")
    
    
#2
# 일주일 간의 날씨 최저온도와 최고온도 정보를 튜플로 생성해 사용한다. 요일명을 입력받아 최저온도와 최고 온도 정보를 출력
temper_dic = {'월': (26, 34), '화': (26, 33), '수': (26, 33), '목': (24, 33), '금': (24, 32), '토': (24, 33), '일': (25, 32)}
day = input("요일명을 한글로 입력하세요 :")
if day in temper_dic :
    print(day,"요일의 최저온도는", temper_dic[day][0],
          "이고 최고 온도는",temper_dic[day][1],"입니다.")
else :
    print(day, "요일의 정보를 찾을 수 없습니다.")
    
    
#3
# 이름을 입력받아 정보를 출력
name_dic = {
    '이름' : '도로시', '나이' : '25',
    '전공' : '수학과', '거주지' : '의왕시',
    '메일주소' : 'abc123@g.com',
    '취미' : ('수영', '독서', '영화나 드라마보기')
}
q = input("이름을 검색하세요 :")
for q in name_dic :
    print(q,":",name_dic[q])
