# 딕셔너리를 선언합니다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임"
}

# 요소 제거전 내용 출력
print("요소 제거전 내용: ", dictionary)

# 딕셔너리의 요소를 제거합니다.
del dictionary["name"]
del dictionary["type"]

# 요소 제거후 내용 출력
print("요소 제거후 내용: ", dictionary)
