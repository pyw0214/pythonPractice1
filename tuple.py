#tuple ()

# a, b = 97, 40

# print(type(divmod(a, b))) # 몫, 나머지

# for i, value in enumerate([1, 2, 3, 4, 5, 6]):
#    print("{}번째 요소는 {}입니다.".format(i, value))


# a = {
#   (0, 0) : 10,
#   (0, 1) : 20,
#   (1, 0) : 30,
#   (1, 1) : 40
# }
# a[0, 0]

#callback

# def call_10_times(func):
#    for i in range(10):
#       #콜백함수(callback)
#       func(i)

# # def print_hello(number):
# #    print("안녕하세요", number)

# call_10_times(lambda number: print("안녕하세요", number)

#Filter함수,  map함수

# def 짝수만(number):
#    return number % 2 == 0
# 짝수만 = lambda number: number % 2 == 0
# a = list(range(100))
# b = filter(짝수만, a)
# print(list(b))

# #map() 


# a = list(range(100))
# #print(list(map(lambda number: number * number, a)))

# print([i * i for i in a if i % 2 == 0])

#함수를 선언합니다.

# power = lambda x: x * x
# under_3 = lambda x: x < 3

# #변수를 선언합니다.

# list_input_a = [1, 2, 3, 4, 5]

# #map()함수를 사용합니다.
# output_a = map(power, list_input_a)
# print("#map()함수의 실행 결과")
# print("map(power, list_input_a): ", output_a)
# print("map(power, list_input_a): ", list(output_a))
# print()






