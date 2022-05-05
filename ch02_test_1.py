# 이름을 입력 받습니다.
user_name = input("성명입력>>  ")
    

#성적을 입력 받습니다.
a = int(input("국어 성적>> "))
b = int(input("영어 성적>> "))
c = int(input("수학 성적>> "))

# 점수를 합산합니다.
result = int(a+b+c) 
   


  
# 출력합니다.    
print("성명:" "{}".format(user_name))
print("국어:" "{}".format(int(a)))
print("영어:" "{}".format(int(b)))
print("수학:" "{}".format(int(c)))
print("총점:" "{}".format(result))

avg = int(result) / float(3) 
print("평균:" "{}".format(avg))


