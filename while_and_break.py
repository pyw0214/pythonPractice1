# i = 0

# while True:
#     print("{} 번째 반복문입니다.".format(i))
#     i += 1

#     input_text =input(">종료하시겠습니까?(y)")
#     if input_text in ["Y", "y"]:
#         print("반복을 종료합니다.")
#         break
# #변수를 선언합니다.
# numbers = [5, 15, 6, 20, 7, 25]

# for number in numbers:
#     #number 가 10보다 작으면 다음 반복으로 넘어갑니다.
#     if number < 10:
#         continue #현재 반복을 중지하고, 다음 반복으로 넘어간다.
#     print(number)

#숫자는 무작위로 입력해도 상관없습니다.

# key_list = ["name", "hp", "mp", "level"]
# value_list = ["기사", 200, 30, 5]
# character = {}

# for i in range(len(value_list)):
#     character[key_list[i]] = value_list[i]

# print(character)


# limit = 1000
# i = 1 

# sum_value = 0
# while sum_value < limit:
#     sum_value += i
#     i += 1

# print("{}를 더할 때  {} 를 넘으며, 그 때의 값은 {} 입니다.".format(i-1, limit, sum_value))


# max_value = 0
# a = 0
# b = 0

# for i in range(1, 99 + 1):
#     j = 100 - i 
  
#     if max_value < i * j:
#         max_value = i * j
#         a = i
#         b = j
# print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))

# print(sum([273, 52, 32, 57, 103]))
# print(max([273, 52, 32, 57, 103]))
#일회용 함수  reversed(), enumerate(), items()

# a ={
#     "key_1" : "value_1",
#     "key_2" : "value_2",
#     "key_3" : "value_3"
# }
# for key, value in a.items():
#     print("{}키의 값은 {}입니다.".format(key, value))

# array = []

# for i in range(0, 20, 2): # [0,2, 4, 6, 8, 10, 12, 14, 16, 18]
#     array.append(i * i)

# array_1 = [i for i in range(10) if i % 3 == 0]


# print(array_1)
output = [i for i in range(1, 100 + 1) if "{:b}".format(i).count("0") == 1]
for i in output:
    print("{}: {}".format(i, "{:b}".format(i)))
print("합계 : {}".format(sum(output)))
# for i in output:
#     print("{} : {}".format(i, "{:b}".format(i)))
# print("합계 :",sum(output))
