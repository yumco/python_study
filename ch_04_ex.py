from datetime import datetime
current_time = datetime.now()


print("어서오세요")
name = input("성명을 입력하세요 >> ")
print(f'{name}님 안녕하세요')

birth_num = int(input("생년을 입력 하세요>> "))
print(f'홍길순님은 현재 {birth_num}입니다')
print(f'홍길순님은{current_time.year}현재 {birth_num}입니다')


age = current_time.year - birth_num + 1

if age <=8:
    print(f'{name}님은 아동입니다')
elif  9<=age<=14:
    print(f'{name}님은 청소년입니다')
elif  15<=age<=24:
    print(f'{name}님은 청년입니다')
else:
    print(f'{name}님은 장년입니다')

