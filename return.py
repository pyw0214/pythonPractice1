#start - end 까지 있는 모든 정수를 더하는 함수
# def sum_all(start, end):
#    변수 = 0
#    for i in range(start, end + 1):
#       변수 += i
#    return 변수

# print(sum_all(1, 100)) #5050

# print(sum_all(50, 100))

# def f_1(x):
#    return (2*x) + 1

# print(f_1(10))

# def f_2(x):
#    return (x ** 2) + (2*x) + 1

# print(f_2(10))

# def mul(*values):
#    변수 = 1
#    for i in values:
#       변수 *= i
#    return 변수

# print(mul(5, 7, 9, 10))


#n! = 1  * 2 * 3 * ...(n-2) * (n-1) * n
# def factorial_1(n):
#    변수 = 1
#    for i in range(1, n + 1):
#       변수 *= i
#    return 변수

# # 3! = 3 * 2 * 1 = 6
# #n! = n * (n-1)!
# #0! = 1
# def factorial_2(n):
#    if n == 0:
#       return 1
#    else:
#       return n * factorial_2(n - 1)

# print(factorial_1(3))
# print(factorial_2(3))

#피보나치 수열

# f(1)=1
# f(2)=1
# f(n)=f(n-1)+f(n-2)
#f(3) = f(2) + f(1) = 2
#f(4) = F(3) + f(2) = 3
# counter = 0
# def f(n):
#    global counter
#    counter += 1
#    if n == 1 or n == 2:
#       return 1
#    else:
#       return f(n - 1) + f(n - 2)
# print(f(20))
# print(counter)

#메모화
# 메모  = {
#    1: 1,
#    2: 1
# }

# def f(n):
#    #변수선언
#    if n in 메모:
#       return 메모[n]
#    output = f(n-1) + f(n-2)
#    메모[n] = output
#    return output

# print(f(150))

#확인문제
# def flatten(data):
#    output = []
#    for item in data:
#       if type(item) == list:
#          output += flatten(item)
#       else:
#          #output.append(item)
#          output += [item]
#    return output


# example = [[1, 2, 3], [4,[5, 6]], 7, [8, 9]]
# print("원본: ", example)
# print("변환: ", flatten(example))

앉힐수있는최소사람수 = 2
앉힐수있는최대사람수  = 10
전체사람수 = 100
memo = {}

def 문제(남은사람수, 앉힌사람수):
   key = str([남은사람수, 앉힌사람수])
   #종료 조건
   if key in memo:
      return memo[key]
   if 남은사람수 < 0:
      return 0
   if 남은사람수 == 0:
      return 1
   #재귀 처리
   count = 0
   for i in range(앉힌사람수, 앉힐수있는최대사람수 + 1):
      count += 문제(남은사람수 - i, i)
   #메모화 처리
   memo[key] = count
   #종료
   return count

print(문제(전체사람수, 앉힐수있는최소사람수))

