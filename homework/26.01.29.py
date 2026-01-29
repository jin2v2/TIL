# 과제 1번
# 아래 함수를 수정하시오.
def check_number():
    try:
        num = int(input("숫자를 입력하세요 : "))
        if num > 0 :
            print("양수입니다.")
        elif num < 0 :
            print("음수입니다.")
        else:
            print("0입니다.")
    except ValueError:
        print("잘못된 입력입니다.")

check_number()

# 과제 2번
class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        try :
            name = input("이름을 입력하세요 : ")
            if not name.strip():
                return None       
            
            age = int(input("나이를 입력하세요 : "))
            

        except ValueError:
            print("나이는 숫자로 입력해야 합니다.")
            return False

        else:
            self.user_data['name'] = name
            self.user_data['age'] = age
            return True

    def display_user_info(self):
        if self.user_data: 
            print(f"사용자 정보 : ")
            print(f"이름: {self.user_data['name']}")
            print(f"나이: {self.user_data['age']}")
        else:
            print("사용자 정보가 입력되지 않았습니다.")
            
# 아래 코드는 수정하지 마세요.
user = UserInfo()
result = user.get_user_info()

if result is True:
    user.display_user_info()
elif result is None:
    # 이름이 입력되지 않은 경우, display_user_info()가 적절한 메시지를 출력해야 합니다.
    user.display_user_info()
# 나이가 잘못 입력된 경우 (result is False), get_user_info()에서 이미 메시지를 출력했으므로
# 추가적인 동작이 필요 없습니다.

# 실습 a번
data = {'name': '홍길동'}
# if not data['age']:
#     print(data['age'])
# else:
#     print('data에는 age라는 키가 없습니다.')
#     data['age'] = 30
#     print(data)
# 아래에 코드를 작성하시오.
try:
    print(data['age'])
except KeyError:
    print('data에는 age라는 키가 없습니다.')
    data['age'] = 30
    print(data)

arr = ['반갑', '하세요', '안녕']
# for i in range(4):
#     print(arr.pop())
# print(arr)
# 아래에 코드를 작성하시오.
try:
    for i in range(4):
        print(arr.pop())
except IndexError:
    print(arr)
    print('더 이상 pop 할 수 없습니다.')

word = '3.15'
# print(int(word))
# 아래에 코드를 작성하시오.
try:
    print(int(word))
except ValueError:
    print('정수로 변환 가능한 값을 입력해 주세요.')

# 실습 b번
class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author
    
class Other(BaseModel):
    TYPE = 'Other Model'
    def save(self):
        print("데이터를 다른 장소에 저장합니다.")

hong = Novel('소설', '홍길동', '고전 소설', 1618, 1692, '허균')
chun = Novel('소설', '춘향전', '고전 소설', 'unknown', 'unknown', '작자미상')
print('Novel 모델 인스턴스의 PK와 save 메서드')
print(hong.PK)
print(chun.PK)
hong.save()
chun.save()
print(hong.author)
print(chun.author)
print('---')

company = Other('회사', '회사명', '회사 설명', 2000, 2023)
print('Other 모델 인스턴스의 PK와 save 메서드')
print(company.PK)
company.save()

print('---')
print('모델 별 타입')
print(Novel.TYPE)
print(Other.TYPE)

# 실습 c번
class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author
    
class Other(BaseModel):
    TYPE = 'Other Model'
    def save(self):
        print("데이터를 다른 장소에 저장합니다.")

class ExtendedModel(Novel, Other):
    def __init__(self, data_type, title, content, created_at, updated_at):
        super().__init__(data_type, title, content, created_at, updated_at)
    
    def display_info(self):
        #print(f"PK: {}, TYPE: {}, Extended Type: {self.extended_type}")
        pass

    def save(self):
        print("데이터를 확장해서 저장합니다.")
    pass

# 새로운 모델 클래스 ExtendedModel을 만든다.
# ExtendedModel은 Novel과 Other 클래스를 다중 상속받아야 한다.
# ExtendedModel은 새로운 속성 extended_type을 가져야 한다.
# ExtendedModel 클래스를 이용하여 새로운 모델 인스턴스 extended_instance를 생성한다.
# ExtendedModel 클래스에 display_info 메서드를 추가한다.

# 이 메서드는 클래스 변수 PK와 클래스 변수 TYPE, 그리고 인스턴스 변수 extended_type을 출력한다.
# ExtendedModel의 save 메서드 호출시 "데이터를 확장해서 저장합니다."를 출력하도록 수정한다.

# extended_instance의 display_info 메서드를 호출하여 정보를 출력한다.
# extended_instance의 save 메서드를 호출하여 저장 메시지를 출력한다.

# 모든 모델 클래스의 인스턴스 생성과 메서드 호출 결과를 확인하여 적절한 출력을 한다

# 실습 1번
# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0


class Dog(Animal):
    def __init__(self):
        Animal.num_of_animal += 1


class Cat(Animal):
    def __init__(self):
        Animal.num_of_animal += 1


class Pet(Dog, Cat):
    @classmethod # 클래스 메서드
    def access_num_of_animal(cls):
        return f' 동물의 수는 {Animal.num_of_animal}마리 입니다.'

dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())

# 실습 2번
# 아래 클래스를 수정하시오.
class Animal:
    pass

class Dog(Animal):
    def bark(self):
        return "멍멍!"


dog1 = Dog()
dog1.bark()

# 실습 3번
# 아래 클래스를 수정하시오.
class Animal:
    pass

class Cat(Animal):
    def meow(self):
        return "야옹!"


cat1 = Cat()
cat1.meow()

# 실습 4번
# 아래 클래스를 수정하시오.
class Animal:
    pass

class Dog(Animal):
    def bark(self):
        return "멍멍!"

class Cat(Animal):
    def meow(self):
        return "야옹!"

class Pet(Dog, Cat):
    def __init__(self, sound):
        self.sound = sound  # 인스턴스 변수 생성
    
    def make_sound(self):
        return self.sound

    def play(self):
        return "애완동물과 놀기"


pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()

# 실습 5번
# 아래 클래스를 수정하시오.
class Animal:
    pass

class Dog(Animal):
    def bark(self):
        return "멍멍!"

class Cat(Animal):
    def meow(self):
        return "야옹!"

class Pet(Dog, Cat):
    def __init__(self, sound):
        self.sound = sound  # 인스턴스 변수 생성
    
    def __str__(self):
        return f"애완동물은 {self.sound} 소리를 냅니다."
    
    def make_sound(self):
        return self.sound

# Dog클래스와 Cat클래스를 다중상속 받는 Pet 클래스를 작성하시오. 
# Pet 클래스에는 __str__ 매직 메서드를 추가하여 객체를 문자열로 표현한다.
# 실행결과 
# 다중 상속시 우선 상속에 따른 출력 결과를 각각 확인하시오.

# Dog Class를 우선 상속하였을 경우
# 애완동물은 멍멍 소리를 냅니다.														
# Cat Class를 우선 상속하였을 경우
# 애완동물은 야옹 소리를 냅니다.								

# 요구사항
# Dog 클래스와 Cat 클래스는 각각 sound 클래스 속성을 가지며, 각 동물의 소리를 나타낸다.
# Pet 클래스는 Dog 클래스와 Cat 클래스를 다중 상속받아야 한다.
# str 매직 메서드를 오버라이딩하여 Pet 객체를 문자열로 표현할 수 있도록 한다.
# __str__메서드는 "애완동물은 {소리} 소리를 냅니다." 형식으로 동물의 소리를 반환해야 한다.
