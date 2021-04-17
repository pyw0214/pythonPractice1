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
   def __del__(self):
      print("객체가 소멸되었습니다.")

   def 출력(self):
      print(self.이름, self.나이)

student = Student("박용욱", 3)
student.출력()




















#클래스(틀): 학생은 이름이라는 속성을 가지고 있어!
# 객체(실체화 된 것): 학생의 이름은 "박용욱"이야!
#실체화 된 객체 = "인스턴스"