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


max_value = 0
a = 0
b = 0

for i in range(1, 99 + 1):
    j = 100 - i 
  
    if max_value < i * j:
        max_value = i * j
        a = i
        b = j

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))