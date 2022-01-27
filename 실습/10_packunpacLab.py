listv3 = [ 'p', 'y', 't', 'h', 'o', 'n' ]

# listv3를 v1, v2, v3, v4, v5, v6에 언패킹해서 저장 한 후, 각 변수의 값을 행 단위로 화면에 출력
v1, v2, v3, v4, v5, v6 = listv3
print(v1);print(v2);print(v3);print(v4);print(v5);print(v6)

# listv3를 언패킹하여 print() 함수에 전달해 출력
print(*listv3)

#listv3를 그냥 print() 함수에 전달해 출력
print(listv3)
