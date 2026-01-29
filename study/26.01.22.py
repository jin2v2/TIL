# 모듈 : 한 파일로 묶인 변수와 함수의 모음

# 모듈 불러오기.
# import (권장 - 명시적으로 불러오기 때문)
# from math import pi, sqrt


# as 클래스를 사용해서 가져올 때 발생하는 충돌을 해결한다.
# from math import sqrt
# from my_math import sqrt as my_sqrt

# 직접 정의한 모듈 사용하기 => 같은 위치에 파일을 생성하고 진행하면 된다.

# 패키지 : 연관된 모듈들을 하나의 디렉에 모아 놓은 것.
# => 폴더를 만들고 그 폴더 내부에 파일을 만들어서 진행.
# ex) my_package 폴더를 만든 후 그 안에 math 폴더와 statics 폴더를 만든 후 각각의 폴더에 파일을 만들고 그 파일에 함수를 작성해서 저장.
# -> 사용 : from my_package.math import my_math
# -> 사용 : from my_package.statics import tools
# print(my_math.add(1,2))
# print(tools.mod(1,2))

# 패키지의 종류 : PSL 내부 패키지
# 파이썬을 설치하면 자동으로 사용할 수 있는 기본 패키지.
# math, os, sys, random 등.. > 설치없이 진행 가능.

# 파이썬 외부 패키지
# 직접 설치해서 진행. 사용할 패키지를 설치할 때는 pip를 사용
# pip : 외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템

# 패키지 설치
# ex) pip install SomePackage(최신버전)
# ex) pip install SomePackage == 1.0.5(특정버전)
# ex) pip install SomePackage > 1.0.4(최소버전)

# requests 외부 패키지 : 파이썬에서 웹에 요청을 보내고 응답을 받는 걸 아주 쉽게 만들어주는 외부 패키지.
# pip install requests
# import requests
# url = "https://~~~"
# response = requests.get(url).json()
# print(response)
# ==> 주어진 url로 요청하는 requests 패키지 메서드 + 문자열로 이루어진 json 자료형을 dict 자료형으로 변환시키는 requests 패키지 메서드

# 패키지 사용 목적 : 모듈들의 이름공간을 구분하여 충돌을 발지.
# 모듈들을 효율적으로 관리하고 할 수 있도록 돕는 역할.

##

# 제어문 : 조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행
# ==> 상황에 따라 다른 코드를 실행하거나, 같은 코드를 여러 번 반복할 수 있게 한다.
# ex) 게임에서 점수가 높으면 "축하합니다!"라는 메시지를 띄우고(조건) 해당 메시지를 5번 깜박이고 싶을때(반복) 사용.

# 조건문 / 반복문
# 조건문 : (if, else, elif) : 주어진 조건식을 평가하여 해당 조건이 참인 경우에만 코드 블록을 실행하거나, 건너뜀
    # 복수 조건문(elif) : (조건이 아니고 다른 조건이면~)
    # 중첩 조건문(if) : if 내부에 또 다른 if 작성. (조건이 맞고 ~ and 느낌)

# 반복문 : (for, while(break, continue)) : 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
    # 1. for
        # 반복가능한 객체의 요소들을 반복하는데 주로 사용.
        # 주로 반복 가능한 객체 요소의 개수만큼 반복 "for i in list():" --> list 내부의 요소만큼 반복. ==> 리스트 순회

        # 반복 가능한 객체의 종류(list, tuple, str(시퀀스 자료형), dict, set(비 시퀀스 자료형))
        # for i=변수 in range(N)=반복 가능한 객체:
            # twinkle(meesage) = 코드블록

        # for문을 통한 리스트 순회 => 리스트 요소 하나씩
            # 인덱스로 리스트 순회 -> for i in range(len(numbers)):
                                    #   numbers[i] = numbers[i] * 2 => 리스트 값이 바뀌게 된다.
                                #   print(numbers)
        # 문자열 순회 -> 글자 하나씩
        # range 순회 -> 범위만큼
        # dict 순회 -> 비시퀀스 자료형. => 반복 순서가 보장되지 않음.

## 중첩 리스트 순회 : 안쪽 리스트 요소에 접근하면 바깥 리스트를 순회하면서 중첩 반복을 사용해 각 안쪽 반복을 순회
# ex) elements = [['A','B'],['c','d']]
#       for elem in elements:
#           for item in elem:
#               print(item)
# 결과) A \n B \n c \n d

###
    # 2. while
        # while 조건이 참인 동안 반복, 조건식이 거짓이 될 때 까지 반복해서 실행
        ## 이때, 코드 블록 실행이 마무리되면서 다시 while 조건식을 확인 한 후 비교했을 때 조건이 거짓이면 종료되는 것.
        # 반복 횟수가 정해지지 않은 경우 주로 사용.
        # 반드시 종료 조건이 필요!! 없으면 무한루프에 빠지게 된다.

# while True :
#   print("계속할까요? (y/n)")
#   answer = input()
#   if answer == 'y':
#       play()
#   else:
#       print("게임을 종료합니다.")
#       break

###

## for 반복문 : 이터러블(반복가능) 요소를 하나씩 순회하면서 반복

## while 반복문 : 주어진 조건식이 참인 동안 반복=반복 횟수가 불명확, 조건에 따라 반복을 종료해야 할 때

##

# 반복 제어 키워드
# break : 해당 키워드를 만나게 되면 남은 코드를 무시하고 반복 즉시 종료. = (종료)
# continue : 해당 키워드를 만나게 되면 다음 코드는 무시하고 다음 반복을 수행. =(무시), 특정 조건은 패스하고 원하는 조건만 출력 가능.
# pass : 아무 동작도 하지 않음. 을 명시적으로 나타내는 키워드

##

### map(function, iterable)
# 반복 가능한 데이터 구조의 모든 요소에 function을 적용하고, 그 결과 값들을 map object로 묶어서 반환
# 결과를 하나씩 꺼내 쓸 수 있는 반복 가능한 객체 자료형.
# 전체 값을 확인하려면 list나 tuple로 형 변환을 해줘야 함.

# ex)
# numbers = [1,2,3]
# result = map(str, numbers)
# print(result)
# print(list(result))

# split() 메서드 : 문자열을 지정한 기준 문자(기본은 공백)를 기준으로 잘라서, 잘린 문자들을 리스트로 반환해주는 문자열 메서드

# zip(*iterables) : 짝지어진 결과(tuple)를 하나씩 꺼내 쓸 수 있는 반복 가능한 객체 자료형
# 전체 값을 확인하려면 list나 tuple로 형변환을 해줘야 함.
# : 여러 개의 반복 가능한 데이터 구조를 묶어서, 같은 위치에 있는 값들을 한의 tuple로 만든 뒤 그것들을 모아 zip object로 반환하는 함수
### 같은 위치에 있는 값들을 묶어줌.

# girls = ['jane', 'ashley']
# boys = ['peter', 'jay']
# pair = zip(girls, boys)
# print(pair)
# print(list(pair))
## 결과 : [('jane', 'peter'), ('ashley', 'jay')]
### 열 정리

# 여러 개의 리스트를 동시에 조회
# for student_scores in zip(kr_scores, math_scores, en_scores):
#   print(student_scores)
# 결과 : 인덱스 1열, 2열, 3열 값들을 1행 2행 3행으로 만들어준다고 생각하면 편할듯...

# 응용: 2차원 리스트 동시에 조회할 때.
# for score in zip(*scores):
#   print(score)
# 결과 : 열을 행으로 나타내준다고 생각하즈아~

##

# for ~ else
# for 루프가 break를 만나 중단되지 않고, 끝까지 정상적으로 완료되었을 때만 else 블록이 실행.
# 만약 break문을 만나면 그대로 종료. else문은 실행되지 않음.

# 예시 : 중복 아이디를 찾았을 경우(break 실행 -> else 실행 안 됨)
# registered_ids = ['admin','user01','guest','user02']
# id_to_check = 'new_user'
# for existing_id in registered_ids :
#   if existing_id == id_to_check
#       print('이미 사용 중인 아이디 입니다.')
#       break
# else:
#   print('사용 가능한 아이디 입니다.')

##

# enumerate(iterable, start=0)
# : 객체의 각 요소에 대해 인덱스와 값을 함께 반환하는 내장함수
# for index, fruit in enumerate(fruits):
#   print(index, fruit)

# enumerate의 index 정보를 이용해 ## 넘버링으로 사용
# start에 시작 값을 설정할 수 있음.
# movies = ['인터스텔라', '기생충', '인사이드 아웃']
# for idx, title in enumerate(movies, start = 1):
#   print(f'{idx}위: {title}')

# 인덱스 정보를 이용해 요소의 ## 위치를 확인할 수 있다.
# respondents = ['은지','정우', '소민', '태호']
# answers = ['', '좋아요', '', '괜찮아요']

# for i, response in enumerate(answers):
#   if response == '':
#       print(f"{respondents[i]} 미제출")

##