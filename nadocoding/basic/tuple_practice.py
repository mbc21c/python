# 튜플은 값을 변경할 수 없지만, 리스트 보다 빠르다.

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)