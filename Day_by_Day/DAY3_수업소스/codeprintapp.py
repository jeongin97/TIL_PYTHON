print("[ 영문 대문자의 코드값 ]")
for munja in range(65, 91) :
    print(munja, hex(munja), bin(munja), chr(munja))

print("[ 영문 소문자의 코드값 ]")
for munja in range(65, 91) :
    print(munja, hex(munja), bin(munja), chr(munja))

print("[ 일부 한글 문자들의 코드값 ]")
for munja in range(44032, 44040) :
    print(munja, hex(munja), bin(munja), chr(munja))

# hex() : 16진법 , oct() : 8진법 , bin() : 2진법 , chr() : 원래문자
