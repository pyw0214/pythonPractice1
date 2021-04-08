#딕셔너리 선언
딕셔너리 = {
    "문자열": "값A", 
    273: [1, 2, 3, 4], 
    True: False, 

}
#반복문 
for key in 딕셔너리:
    print("{} : {} ".format(key, 딕셔너리[key]))

#요소추가
딕셔너리["키"] = "값"
print()
for key in 딕셔너리:
    print("{} : {} ".format(key, 딕셔너리[key]))
#$요소제거
del 딕셔너리["키"]
print()
for key in 딕셔너리:
    print("{} : {} ".format(key, 딕셔너리[key]))