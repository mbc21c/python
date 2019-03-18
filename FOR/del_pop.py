list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")

## 제거 방법[1] - del

del list_a[1]
print("del list[1]:", list_a)

## 제거방법[2] - pop()
list_a.pop(2)
print("pop(2):", list_a)
print()

list_b = [0, 1, 2, 3, 4, 5, 6]
del list_b[3:6]

print("# 인덱스로 리스트의 요소 여러개 제거하기")
print("del list_b[3:6]:", list_b)

list_c = [0,1,2,3,4,5,6]
list_d = [0,1,2,3,4,5,6]
del list_c[:3]
del list_d[3:]

print("# 인덱스로 리스트의 요소 한쪽 전부 제거하기")
print("del list_c[:3]:", list_c)
print("del list_d[3:]:", list_d)
