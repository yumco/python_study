

number_1 = input("첫번째 정수 입력 >> ")
number_2 = input("두번쨰 정수 입력 >> ")
number_3 = input("세번째 정수 입력 >> ")

# 리스트를 만들고 최대 값 최소 값을 찾습니다
number_list = [number_1, number_2, number_3]
max_number = max(number_list) 
min_number = min(number_list)



#출력합니다
print(f'가장 큰 수는 {max_number}입니다')
print(f'가장 작은 수는 {min_number}입니다')