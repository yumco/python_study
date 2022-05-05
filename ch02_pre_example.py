print(":::나는 65세까지 몇년 남았을까?:::")
user = input("성명입력>  ")
age = int(input("나이입력> "))
futurge = 65-age
print("{:-^30}".format("입력정보확인"))
print("{}님은 65세까지 {}년 남았습니다.".format(user, futurge))