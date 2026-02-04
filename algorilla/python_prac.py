# 리스트 (sequential), mutable : 가변
odd = [1, 2, 3, [4, "short"]]
# 리스트 안에는 어떠한 자료형도 포함할 수 있다.

odd[1]
odd[0] + odd[1]
odd[-1]

# 에러 발생 odd[1] + odd[3]
# int와 list는 더할 수 없다.

odd[-1][0]

# 삼중 리스트에서 인덱싱
a = [1, 2, ['a', 'b', ['life', 'is']]]
a[2][2][0]

# 리스트의 슬라이싱
a[0:2]

# 문자열 슬라이싱
b = "123456"
b[0:2]

# 중첩된 리스트에서 슬라이싱하기.
x = [1,2,3,['a','b','c'],4,5]
x[2:5]
x[3][:2]

# 리스트 연산하기.
a = [1,2,3]
b = [4,5,6]
# 리스트 더하기 a+b
# 리스트 반복하기 a*3
# 리스트 길이 구하기 len(a)

# a = [1,2,3]
# a[2] + "hi" --> 연산 오류 발생!!
# --> 해결법!
str(a[2]) + "hi"
# str은 정수나 실수를 문자열로 바꿔주는 함수.

### 리스트의 수정과 삭제
# 리스트는 값을 수정하거나 삭제할 수 있다.
a = [1,2,3]
a[2] = 4
a

a = [1,2,3]
del a[1] # del a[x]는 x번째 요솟값을 삭제한다.
del a[2:]
a

### 리스트 관련 함수
# append : 리스트에 요소 추가
# sort : 리스트 정렬
# reverse : 리스트 뒤집기
# index : 인덱스 반환 - 리스트에 x값이 있으면 x의 위치값 반환.
# insert : 리스트에 요소 삽입
# remove : 리스트 요소 제거 - 첫 번째로 나오는 x값 제거.
# pop : 리스트 요소 끄집어 내기 - 마지막 요소 반환 후 그 요소 삭제.
# count : 리스트에 포함된 요소 x의 개수 세기
# extend : 리스트 확장
a = [1,5,8,3]
a.append(4)
a.sort()
a.reverse()
a.index(1) # x값이 존재하지 않으면 오류 발생.
a.insert(0,9)
a.insert(4,2)
a.remove(4)
a.pop()
a.pop(2) # x번째 요소 반환하고 그 요소 삭제.
a.count(2)
a.extend([3,4,5])
b=[8,9]
a.extend(b)
a
#################################################
# 튜플(sequential) : 불변
# 리스트와 공통점 : 인덱싱 가능(순서가 있다), 슬라이싱 가능, 튜플 연산 가능(튜플 내의 값 연산 x)
# 리스트와 차이점 : 요소값을 바꿀 수 없다. = 바뀌지 않음.
t1 = ()
t2 = (1,) # 1개의 요소만을 가질 때는 요소 뒤에 , 필수.
t3 = (1,2,3)
t4 = 1,2,3 # 괄호 생략가능
t5 = ('a','b',('ab','cd'))
#################################################
# 딕셔너리(key를 통해 value값을 얻는다.)
# 딕셔너리 = 대응 관계를 나타내는 자료형, 연관배열, 해시
# 가변

dic = {'name' : 'jin', 'birth' : '000519'}
a = {1 : 'hi'}
a = {'a' : [1,2,3]}

# 딕셔너리 쌍 추가, 삭제
a = {1 : 'a'}
a[2] = 'b'
a['name'] = 'jin'
a[2] = 'c'
a[3] = [1,2,3]
a

del a[1] # del a[key]를 입력해서 삭제.
a

# 키를 사용해서 값 얻기
grade = {'pey' : 100, 'jin' : 90}
grade['pey']

# 딕셔너리는 리스트나 튜플에 있는 인덱싱 방법을 적용할 수 없다.
# 동일한 키가 중복으로 존재할 수 없다.
# 키에 리스트는 사용 할 수 없다.
# 키에 튜플은 사용 가능하다.
# 키의 기준 : 변하지 않는(immutable) 값이어야 한다.
# 값에는 변하든 변하지 않든 아무 값이나 넣을 수 있다.

grade.keys()
grade.values()
grade.items()

for i in grade.keys():
    print(i)

list(grade.keys())

# 딕셔너리 초기화
grade.clear()
grade

# 키로 값 얻기 get 이용.
grade.get('pey')

# 그러면 grade['pey']와 grade.get('pey')의 차이는?
# --> grade['pey']는 존재하지 않을 시 오류 발생
# --> grade.get('pey')는 None 반환

# 키가 없을 때 디폴트 값으로 반환
grade.get('nokey', 'NOT FOUND')

# 해당 키가 딕셔너리 안에 있는지 조사하기
'name' in grade
'pey' in grade

# 키로 값 얻기 pop 이용.
pey = grade.pop('pey')
pey

joon = grade.pop('joon', 'NOT FOUND')
joon

grade
#################################################
# 집합(set)
# 중복을 허용하지 않고, 순서가 없는 데이터의 모임
# 집합 연산을 처리.
# 데이터 중복 제거용 필터로 종종 사용.
# 순서가 없다 ==> 인덱싱을 통해 요솟값을 얻을 수 없다.
# ==> 집합 자료형에 저장된 값을 인덱싱으로 접근하려면
# => 리스트나 튜플로 변환한 후 접근.
s0 = set()
s1 = set([1,2,3])
s1
s2 = set("Hello")
s2
s3 = {1,2,3}
s3
s4 = {'a','b','c'}
s4

ss1 = set([1,2,3])
l1 = list(ss1)
l1[0]

t1 = tuple(ss1)
t1
t1[0]

# 교집합, 합집합, 차집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합
s1 & s2
s1.intersection(s2)

# 합집합
s1 | s2
s1.union(s2)

# 차집합
s1 - s2
s1.difference(s2)

# 집합 자료형 관련 함수
# 값 1개 추가하기
s1 = set([1,2,3])
s1.add(4)
s1
# 값 여러 개 추가하기
s1.update([4,5,6])
s1
# 특정 값 제거하기
s1.remove(2)
s1
# 특정 값 제거하기2
# 존재하지 않는 값을 제거해도 오류 발생 X
s1.discard(9)
s1
# 모든 값 제거하기
s1.clear()
s1
#################################################
# for문
# for 변수 in 리스트(또는 튜플, 문자열):
#    수행할_문장1
#    수행할_문장2

# enumerate 함수
# : 리스트의 순서와 값을 함께 구할 수 있음.
fruits = ['orange', 'apple', 'banana']

for i, fruit in enumerate(fruits, 1):
    print(f"{i}: {fruit}")

# zip 함수
# : 두 개 이상의 리스트를 동시에 순회하고 싶을 때
names = ['홍길동', '김철수', '이영희']
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}점")

# 함수 : 
# def 함수_이름(매개변수):
#    수행할_문장1
#    수행할_문장2
def add(a,b):
    return a+b
add(3,4)
print(add(4,5))

# 가변 매개변수
# 매개변수 이름 앞에 *를 붙이면 입력값을 전부 모아 튜플로 만들어준다.
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print(add_many(1,2,3,4,5))

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

print(add_mul('add',1,2,3,4,5))
print(add_mul('mul',1,2,3,4,5))

# 키워드 매개변수, kwargs, 
# 매개변수 이름 앞에 **를 붙이면 매개변수는 딕셔너리가 된다.
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name = 'koo', age=3)

def create_profile(**info):
    print("=== 프로필 정보 ====")
    for key, value in info.items():
        print(f"{key}: {value}")

create_profile(이름="김철수", 나이=35, 직업="프로그래머")

# 일반 매개변수, 가변 매개변수, 키워드 매개변수 모두 함께 사용
def mixed_function(name, *args, **kwargs):
    print(f"이름: {name}")
    print(f"추가 인수들: {args}")
    print(f"키워드 인수들: {kwargs}")

mixed_function("홍길동", 1,2,3, age=25, city="seoul")

# 함수의 반환값은 언제나 하나이다.
# return문을 만나는 순간, 반환값을 반환한 다음 함수를 빠져나간다.
# 초기화하고 싶은 매개변수는 항상 뒤쪽에 놓아야한다.

# 리스트나, 딕은 함수 안에서 값을 변경하면 원래 자료도 함께 변경된다.
# --> 변경 가능한 자료형이기 때문.

# lambda 함수
add = lambda a, b: a+b
result = add(3,4)
print(result)

# lambda로 만든 함수는 return 명령어가 없어도 표현식의 결과값을 반환한다.

# 함수의 독스트링
# 함수에 대한 설명을 문서화하는 방법
def add(a,b):
    """
    두 숫자를 더하는 함수
    
    Parameters:
    a (int, float): 첫 번째 숫자
    b (int, float): 두 번째 숫자
    
    Returns:
    int, float: 두 숫자의 합
    """
    return a+b
# 독스트링 확인하기
print(add.__doc__)

#클래스
class FourCal:
    def __init__(self, first, second): # 생성자
        self.first = first
        self.second = second

    def add(self): # 클래스 안에 구현된 함수 = 매서드
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a =FourCal(4, 2)
b =FourCal(3, 8)
a.add()
b.mul()

# setdata와 같은 초깃값을 설정해야 할 필요가 있을 때는
# 메서드를 호출하여 초기값을 설정하기보다 생성자를 구현하는 것이 안전함.

# 생성자 : __init__
# : 객체가 생성될 때 자동으로 호출되는 메서드.

# 상속
# MoreFourCal 클래스는 FourCal 클래스를 상속했으므로
# FourCal 클래스의 모든 기능을 사용할 수 있다.
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    
a = MoreFourCal(4,2)
a.add()
a.pow()

# 메서드 오버라이딩
# : 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만든 것.
# 부모 클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4,0)
a.div()

# 객체 변수
# : 다른 객체들의 영향을 받지 않고 독립적으로 그 값을 유지한다

# 클래스 변수
# : 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 선언하여 생성.
# : 객체변수와 달리 클래스로 만든 모든 객체에 공유된다는 특징이 있다.
class Family:
    lastname = "김"
    
Family.lastname
a = Family()
b = Family()
a.lastname
b.lastname

# Family 클래스의 lastname을 박으로 변경
Family.lastname = "박"
a.lastname

# 클래스 변수와 동일한 이름의 객체 변수를 생성
# Family 클래스의 lastname이 바뀌는 것이 아니라
# a객체에 lastname이라는 객체변수가 새롭게 생성된 것.
# 즉, 객체변수는 클래스변수와 동일한 이름으로 생성할 수 있다.
a.lastname = "최"
a.lastname

# 모듈
# : 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일.
# .py로 만든 파이썬 파일은 모두 모듈.
# import mod1
# print(mod1.add(3,4))
# print(mod1.sub(5,4))

# from mod1 import *
# from mod1 import add, sub
# print(add(4,5))

# import mymod.mod2 as mod2
# print(mod2.PI)
# a = mod2.Math()
# print(a.solv(2))

import sys
# sys 모듈을 사용하면 파이썬 라이브러리가 설치되어있는 디렉 확인 할 수 있다.
sys.path
sys.path.append("C:/Users/USER/Desktop/ssafy_python/mymod")
sys.path

# 패키지
# : 관련 있는 모듈의 집합
# : 패키지 구조로 모듈을 만들면 다른 모듈과 이름이 겹쳐도 안전하게 사용할 수 있다.
