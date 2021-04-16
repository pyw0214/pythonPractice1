#함수 내부 : return
#반복문 내부: break

# try:
#    #예외 발생 가능성 있는 코드
#    number = int(input("> 정수 입력"))
#    print("입력 값은 {} 입니다.".format(number))
# except:
#    #예외 발생 시 실행할 코드
#    print("예외가 발생했습니다.")

# finally: 
#    #무조건적으로 실행하는 코드
#    print("무조건적으로 실행됩니다.")

#test()함수를 선언
# while True:
#    print("test() 함수의 첫 줄입니다.")
#    try:
#       print("try 구문이 실행되었습니다.")
#       break
#       print("try 구문의 return 키워드 뒤입니다.")
#    except:
#       print("except 구문이 실행되었습니다.") 
#       break
#    finally:
#       print("finally  구문이 실행되었습니다.")
#    print("test() 함수의 마지막 줄입니다.")

# try:
#    a = [272, 103, 52, 42, 100]
#    number = int(input("정수 입력(0~4까지 입력해주세요.)>"))
#    print(a[number])
# except ValueError as exception:
#    print("값에 문제가 있습니다.")
# except IndexError as exception:
#    print("0~4까지 입력 부탁드립니다. ")
# except Exception as exception:  # !! 
#    print("알 수 없는 에러 발생")
#  # 개발자에게 메일을 보낸다. 등등.. 

#raise 에외 객체
raise Exception("안녕하세요")
raise ValueError("ㅇㅂㅇ")
