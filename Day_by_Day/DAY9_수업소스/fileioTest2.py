f = None

try:
    f = open("live.txt", "rt", encoding="UTF-8")
    print(f, type(f))
    text = f.read()
    print(text)
except FileNotFoundError as e:
    print("파일이 없습니다. - ", e)
finally:
  if f :
      print("파일 닫을게요")
      f.close()
  else :
      print("열리지도 않네요")
'''
print("*"*20)
f = None
try:
    f = open("live.txt", "rt", encoding="utf8")
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    if f :
        f.close()
'''
help(open)
help(f.read)
