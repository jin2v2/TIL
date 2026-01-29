# 과제 1번
def remove_duplicates_to_set(lst):
    return set(lst)

result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)

# 과제 2번
def add_item_to_dict(dictionary,key,value):
    new_dict = dictionary.copy()
    new_dict.setdefault(key,value)
    #new_dict[key] = value

    return new_dict


#def add_item_to_dict(dictionary, key, value):
#    return {**dictionary, key: value}


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)

# 실습 a번
my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

# 아래에 코드를 작성하시오.
for key in my_set:
    print(my_dict.get(key))

var = (1, 2, 3, 'A')
value = '변수로도 키 설정 가능'
my_dict[var] = value
print(my_dict)

# 실습 b번
data = {
    '이름': '키위',
    '종류': '새',
    '원산지': '호주' 
}

plus_data = {
    '종류': '과일',
    '가격': 30000
}
# 1. data가 가진 모든 키와 벨류 목록을 출력한다.
data.items()
# 2. data가 가진 벨류 목록들만 모아서 출력한다.
data.values()
# 3. data에서 'without' 키가 가진 value를 출력한다.
    # 해당하는 키가 data에 없다면, 'unknown' 문자열을 출력한다.
data.setdefault('without','unknown')
# 4. plus_data가 가진 모든 키와 벨류를 data에 추가한다.
data.update(plus_data)
# 5. 변경된 data를 출력한다.
print(data)

# 실습 c번
data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.
for item in data:
    for key in key_list:
        item.setdefault(key, 'unknown')
        value = item.get(key)
        print(f'{key} 은/는 {value}입니다.')

# 실습 1번
# 아래 함수를 수정하시오.
def union_sets(set1, set2):
    return set1.union(set2)

def union_multiple_sets(*sets):
    if len(sets) < 2:
        print("최소 두 개의 셋이 필요합니다.")
        return
    return set.union(*sets)


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)  # {1, 2, 3, 4, 5}

result = union_multiple_sets({1, 2}, {3, 4}, {5, 6})
print(result)  # {1, 2, 3, 4, 5, 6}

result = union_multiple_sets({1, 2})
# 출력 : 최소 두 개의 셋이 필요합니다

# 실습 2번
# 아래 함수를 수정하시오.
def get_value_from_dict(dict1, key):
    return dict1.get(key, 'Unknown')


my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)  # Alice

result = get_value_from_dict(my_dict, 'gender')
print(result)  # Unknown

# 실습 3번
# 아래 함수를 수정하시오.
def intersection_sets(set1, set2):
    intersection = set1 & set2

    if len(intersection) == 0: # not intersection 도 가능
        print("공통 요소가 없습니다")
        return 0, set()

    return len(intersection), intersection

result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result)  # (1, {3})

result = intersection_sets({1, 2}, {3, 4})
print(result)  # (0, set())
# 출력: 공통 요소가 없습니다

# 실습 4번
# 아래 함수를 수정하시오.
def get_keys_from_dict(dict1):
    return dict1.keys()

def get_all_keys_from_dict(dictionary):
    result = []

    for key in dictionary:
        result.append(key)

        value = dictionary[key]
        
        if type(value) == dict:
            result.extend(get_all_keys_from_dict(value))

    return result

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

my_dict = {'person': {'name': 'Alice', 'age': 25}, 'location': 'NY'}
result = get_all_keys_from_dict(my_dict)
print(result)  # ['person', 'name', 'age', 'location']

# 실습 5번
def ordered_difference_sets(set1, set2):
    diff1 = set1 - set2
    diff2 = set2 - set1

    # 길이 비교
    if len(diff1) <= len(diff2):
        return diff1, diff2
    else:
        return diff2, diff1
    
# 예시 실행
result = ordered_difference_sets({1, 2, 3, 4}, {3, 4, 5, 6})
print("결과:", result)  # 출력: ({1, 2}, {5, 6})

result = ordered_difference_sets({1, 2, 3, 4}, {1, 2, 3})
print("결과:", result)  # 출력: (set(), {4})

