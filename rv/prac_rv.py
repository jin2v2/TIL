# 1. 평균 값 구하기
def calculate_avg(temperatures):
    total = 0
    count = 0
    for i in temperatures:
        count += 1
        total += i
    return total

# 2. min_length 보다 큰 길이를 가지는 요소의 수
def count_long_words(words, min_length):
    # 리스트를 순회하면서 리스트 내부에 문자열도 순회.
    # 요소의 총 합을 받을 변수 생성
    # 문자열의 길이를 받을 변수 생성
    # min_length와 길이 비교 후 요소의 수 합
    count = 0
    for i in words:
        word_length = 0
        
        for _ in i: # 리스트 내부의 문자열의 길이 확인
            word_length += 1
        
        if word_length >= min_length:
            count += 1
    
    return count

# 3. 리스트 역순
def reverse_list(visited_items):
    # 빈 리스트를 만들어서 역순으로 받은 뒤 출력
    reverse = []
    for i in range(len(visited_items)-1,-1,-1):
        reverse.append(visited_items[i])
    return reverse

# 4. 주문 수
def count_menus(orders):
    # 빈 딕을 만들어서 순회한다. 
    # 이때 기존에 없으면 추가, 있으면 +1
    reverse = {}
    for i in orders:
        if i in reverse:
            reverse[i] += 1
        else:
            reverse[i] = 1
    return reverse
    
# 5. 이중 리스트에서 0이 아닌 값들의 개수
def count_total_items(warehouse):
    # 0이 아닌 값들의 개수를 구하는 count 변수 생성
    count = 0
    for i in warehouse:
        for j in i:
            if j != 0:
                count += 1
    return count

# 6. 이중 리스트에서 각 리스트의 최댓값들의 합
def sum_row_maximums(matrix):
    # 총 합을 구할 변수, 최댓값을 받을 변수
    total = 0
    for i in matrix:
        max_val = i[0]
        for j in i:
            if max_val < j:
                max_val = j
        total += max_val
    return total

# 7. 딕셔너리 활용해서 ~
def categorize_books(books):
    # 빈 딕셔너리를 만들어서
    # key, val 값 재설정 후
    # 이미 있으면 +1
    # 없으면 추가
    book_dict = {}
    for i in books:
        key, val = i['category'], i['title']

        if key in book_dict: # 이미 있으면 새로 만든 딕셔너리에 +
            book_dict[key].append(val)

        else: # 없으면 추가
            book_dict[key] = [val]
    return book_dict

# 8. 정렬 후 2번째로 큰 값
def find_second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers[-2]
