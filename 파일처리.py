'''
with open("test.txt", "a") as file:
   file.write("안녕하세요.")

file = open("test.txt", "a")
file.write("안녕하세요.")
file.close()

with open("test.txt", "r") as file:
   print(file.read())

# file = open("test.txt", "r")
# print(file.read())
# file.close()
'''




'''
어떤 대상 (!)
-텍스트 파일: 텍스트 에디터로 열 수 있는 것
-바이너리 파일: 0101010001   ___열 수 없는 것 (이미지, 동영상, word,excel, PDF 등)

어떻게 다룰 것인가(!)
-쓰기
 - 새로 (write): w
 - 이어 쓰기 (append) : a 
-읽기(read): r
'''
#랜덤하게 1000명의 키와 몸무게 만들기

#랜덤한 숫자를 만들기 위해 가져옵니다.
import random

#간단한 한글 리스트를 만듭니다.
hanguls = list("가나다라마바사아자차카타파하")
#파일을 쓰기 모드로 엽니다.
with open("info.txt", "w") as file:
   for i in range(1000):
      #랜덤한 값으로 변수를 생성합니다.
      name = random.choice(hanguls) + random.choice(hanguls)
      weight  = random.randrange(40, 100)
      height = random.randrange(140, 200)
      #텍스트를 씁니다.
      file.write("{}, {}, {}\n".format(name, weight, height))