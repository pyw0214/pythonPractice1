# a = ['수박','바나나','키위', 1, 2, True]
# a[0]
# print(a[0])
# print(a[-1])
# a = [[1,2,3],[4,5,6],[7,8,9]]

# print(a[0: 1000000])

# print(1 in [1,2,3])

# a = "hello"
# b = a.upper()
# print(b)

# a = [1, 2, 3 ]
# b = a + [4]

# print(b)
#20210410
#range <= 자료형!

#range(시작, 끝, 단계) 
# range(0, 10, 1)
# print(list(range(10)))

# array = [273, 52, 103, 32, 57]


# for i in reversed(array):
#     print(i)

#while

import time 

처음 = time.time()

while  처음 + 5 > time.time():
    pass

print("프로그램이 종료되었습니다.")