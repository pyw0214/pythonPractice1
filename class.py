'''
객체(object)
= 속성 + 행위

사람
 - 이름, 키, 나이, 생년월일, 머리카락의 개수 등등
 - 달린다, 걷는다, 잔다, 프로그래밍을 한다 등등
 - x : 행위(?) 
 학생 성적
 - 
 '''

def 학생_생성(name, korean, math, english, science):
   return {
      "name": name,
      "korean": korean,
      "math": math,
      "english": english,
      "science": science
   }

def 총점(student):
   return student["korean"] + student["math"] + \
      student["english"] + student["science"]
def 평균(student):
   return 총점(student) / 4
def 출력(student):
   print(student["name"], 총점(student), 평균(student), sep = "\t")


#학생 리스트를 선언합니다.
students = [
   학생_생성("윤인성", 87, 92, 100, 95),
   학생_생성("박용욱", 84, 88, 100, 98),
   학생_생성("박지은", 95, 97, 85, 62),
   학생_생성("박성국", 90, 90, 90, 90),
   학생_생성("박지영", 92, 100, 82, 93),
   학생_생성("유현주", 95, 95, 82, 100) 
]
#학생을 한 번씩 반복합니다.
print("이름", "총점", "평균", sep = "\t")
for student in students:
   출력(student)
   """
   #점수와 총합의 평균을 구합니다.
   score_sum = student["korean"] + student["math"] + \
      student["english"] + student["science"]
   score_average = score_sum / 4
   #출력합니다.
   print(student["name"], score_sum, score_average, sep = "\t")
   """
class 학생:
   def __init__(self, name, korean, math, english, science):
      self.name = name
      self.korean = korean
      self.math = math
      self.english = english
      self.science = science
   def 총점(self):
      return self.korean + self.math + self.english + self.science
   def 평균(self):
      return self.총점() / 4
   def 출력(self):
      print(self.name, self.총점(), self.평균(), sep = "\t")


students = [
   학생("윤인성", 87, 92, 100, 95),
   학생("박용욱", 84, 88, 100, 98),
   학생("박지은", 95, 97, 85, 62),
   학생("박성국", 90, 90, 90, 90),
   학생("박지영", 92, 100, 82, 93),
   학생("유현주", 95, 95, 82, 100) 
]

print("이름", "총점", "평균", sep = "\t")
for student in students:
   student.출력()

#객체 지향 프로그래밍 언어

동사 + 목적어 : 명령어
print("ㅇㅂㅇ")

주어 + 동사 + 목적어 : 주어가 행위를 한다.
- 학생.출력()
- 학생.평균()
- 학생.총합()