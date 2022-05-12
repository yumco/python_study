#선언합니다.
pi = 3.141592
r= int(input("원의 반지름을 입력하세요>>"  ))

#계산식입니다.
line = 2 * pi * r
area = pi * r * r

#출력합니다.
print("반지름이 {}인 원의 둘레의 길이는 {} 이고 넓이는{} 입니다.".format(r, line, area))
