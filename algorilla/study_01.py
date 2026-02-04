bloods = ['B','AB','A','AB','B','B','B','A','O','B']
# blood_dict = {'A':2,'B':5,'O':1,'AB':2}

blood_dict = {}
for key in bloods:
    if key in blood_dict:
        blood_dict[key] += 1
    else:
        blood_dict[key] = 1

print(blood_dict)


data_list = [
    {'name':'정도윤', 'blood':'B'},
    {'name':'강하은', 'blood':'AB'},
    {'name':'최서윤', 'blood':'A'},
    {'name':'조도윤', 'blood':'AB'},
    {'name':'이서윤', 'blood':'B'},
    {'name':'최민준', 'blood':'B'},
]

# blood_dict = {'A':['최서윤','최도윤'], 'B':['정도윤', '이서윤', '최민준'],}

blood_dict = {}

for item in data_list:
    key, val = item['blood'], item['name']
    if key in blood_dict:
        blood_dict[key].append(val)
    else:
        blood_dict[key] = [val]
print(blood_dict)

####

def recur_example(number):
    if number == 1:
        return 1
    else:
        return number + recur_example(number - 1)
result_1 = recur_example(5)
print(result_1) # 5 + 4 + 3 + 2 + 1 = 15

# 거듭 제곱 재귀 함수
# base = 밑, exponent = 지수
# base의 exponent승 == 2의 3승
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        
        return base * power(base, exponent-1)
result_2 = power(2, 3)
print(result_2) # 2 * 2 * 2 * 1 = 8

# 모든 자릿수 더하기 함수
def sum_of_digits(number):
    if number < 10:
        return number
    else:
        return sum_of_digits(number % 10) + sum_of_digits(number // 10)
result_3 = sum_of_digits(321)
print(result_3) # 1 + 2 + 3 = 6