# RE : ) 2, 3, 4, 6, 7 
# 2번
# min_length 보다 큰 문자열의 길이의 개수
def count_long_words(words, min_length):
    # 문자열의 길이를 받을 변수
    # ~보다 긴 문자의 개수를 받을 변수
    count = 0
    for i in words:
        str_length = 0
        for _ in i:
            str_length += 1
            if str_length >= min_length:
                count += 1
    return count

# 3번 리스트 역순
def reverse_list(visited_items):
    # 빈 리스트를 만든 후 그 곳에 역순으로 append
    reverse = []
    for i in range(len(visited_items)-1, -1, -1):
        reverse.append(visited_items[i]) # 입력값을 역순으로 하나씩 append
    return reverse

# 4번
# 주문 횟수 구하기
def count_menus(orders):
    # 빈 딕셔너리를 구한 뒤
    # 만약 입력값이 딕셔너리에 있으면 +1 없으면 1(추가)
    order_dict = {}
    for i in orders:
        if i in order_dict:
            order_dict[i] += 1
        else:
            order_dict[i] = 1
    
    return order_dict
        

# 6번


# 7번