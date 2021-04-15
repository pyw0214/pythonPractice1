#구문 오류  
#코드에 문제가 있어서 
#실행 X
# print("실행되었습니다")
# print("ㅇㅂㅇ)





# #예외 처리 (런타임 오류)
# #코드 자체 문법적 오류 X
# #실행과 관련된 문제
# #실행O 죽음
# print("실행되었습니다.")
# list_a = [1, 2, 3]
# print(list_a[100])

#숫자를 입력받습니다.
# while True:
#    string_input = input("정수 입력 >")
#    if string_input.isdigit():
#       number_input_a = int(string_input)
#       #출력합니다.
#       print("원의 반지름: ", number_input_a)
#       print("원의 둘레: ", 2 * 3.14 * number_input_a)
#       print("원의 넓이: ", 3.14 * number_input_a * number_input_a)
#       break
#    else:
#       print("정수를 입력해주세요!")

# #try, except 구문
# while True:
#    try:
#       #예외 발생 가능한 코드
#       print(float(input(">숫자를 입력해주세요: "))**2)
#       break
#    except:
#       #예외 발생 시 실행할 코드3
#       pass

#변수를 선언합니다.
# list_input_a = ["52", "273", "32", "스파이", "100"]

# #반복을 적용합니다.
# list_number = []
# for item in list_input_a:
#    #숫자로 변환해서 리스트에 추가합니다.
#    try:
#       float(item)
#       list_number.append(item)
#    except:
#       pass
# #출력합니다.
# print("{} 내부에 있는 숫자는".format(list_input_a))
# print("{}입니다.".format(list_number))

numbers = [52, 273, 32, 103, 90, 10, 275]

print("# (1) 요소 내부에 있는 값 찾기")
print(" - {}는 {} 위치에 있습니다.".format(52, numbers.index(52)))
print()

print("# (2) 요소 내부에 없는 값 찾기")
number = 10000
try:
   print(" - {}는 {}위치에 있습니다.".format(number, numbers.index(number)))
except:
   print("-리스트 내부에 없는 값입니다.")
print()

print("---정상적으로 종료되었습니다.---")