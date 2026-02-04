# 1번
def calculate_avg(temperatures):
    return sum(temperatures) / len(temperatures)

def calculate_avg(temperatures):
    count = 0
    total = 0
    for val in temperatures:
        # 개수, 합을 계산
        count += 1
        total += val

    return total / count

# 2번
def count_long_words(words, min_length):
    
    count = 0
    # words 리스트의 모든 단어들의 길이 조사
    for word in words:
        # print(word, len(word))
        word_length = 0

        for _ in word:
            word_length += 1

        #if len(word) >= min_length:
        #    count += 1

        if word_length >= min_length:
            count += 1

    return count

# 3번
def reverse_list(visited_items):
    result = []
    for i in range(len(visited_items)-1, -1, -1):
        result.append(visited_items[i])
    return result

def reverse_list(visited_items):
    return visited_items[::-1]

# 4번
def count_menus(orders):
    order_dict = {}
    for key in orders:
        if key in order_dict:
            order_dict[key] += 1
        else:
            order_dict[key] = 1

    return order_dict

from collections import defaultdict
def count_menus(orders):
    order_dict = defaultdict(int)
    for key in orders:
            order_dict[key] += 1
        
    return order_dict

# 5번
def count_total_items(warehouse):
    count = 0
    for items in warehouse:
        for item in items:
            if item != 0:
                count += 1

    return count 

# 6번
def sum_row_maximums(matrix):
    result = 0
    for row in matrix:
        # row 에서 최대값 찾기
        max_val = row[0]
        for val in row:
            if max_val < val:
                max_val = val
    
        result += max_val
    
    return result

def sum_row_maximums(matrix):
    result = 0
    for row in matrix:
        result += max(row)
        
    return result

# 7번
def categorize_books(books):
    book_dict = {}
    for book in books:
        key, val = book['catrgory'], book['title']
        if key in book_dict:
            book_dict[key].append(val)
        else:
            book_dict[key] = [val]

    return book_dict

# 8번
def find_second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort() # 오름차순

    # numbers.sort(reverse=True) # 내림차순
    # return numbers[1]
    return numbers[-2]

# 9번

# 10번
