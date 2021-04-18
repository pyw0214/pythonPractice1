#스네이크케이스 & 캐멀케이스

#I_love_you.

#스네이크 케이스
#I_love_you :  기본적으로 사용
#I_LOVE_YOU : 상수를 표현[]
 
#캐멀케이스

#ILoveYou: 클래스 이름
#ILoveYou: 대문자로시작

#Student(= 클래스 이름)

class Student:
   def __init__(self, 이름, 나이):
      print("객체가 생성되었습니다.")
      self.이름 = 이름
      self.나이 = 나이

   def __eq__(self, other):
      return self.나이 == other.나이 and \
         (self.이름 == other.이름)
   def __nq__(self, other):
       return self.나이 != other.나이
   def __gt__(self, other):
       return self.나이 > other.나이
   def __ge__(self, other):
       return self.나이 >= other.나이
   def __lt__(self, other):
       return self.나이 < other.나이
   def __le__(self, other):
       return self.나이 <= other.나이


student = Student("박용욱", 3)
print(student == student)
print(student != student) 
print(student > student)   #greater than
print(student >= student)  #greater than or equal to
print(student < student)
print(student <= student)




















#클래스(틀): 학생은 이름이라는 속성을 가지고 있어!
# 객체(실체화 된 것): 학생의 이름은 "박용욱"이야!
#실체화 된 객체 = "인스턴스"