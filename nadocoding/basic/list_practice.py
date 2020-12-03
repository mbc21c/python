# # 리스트 []

# # 지하철 칸별로 10명,20명,30명

# # subway1 = 10
# # subway2 = 20
# # subway3 = 30

# subway = [10,20,30]

# print(subway)

# subway = ["유재석","조세호","박명수"]

# print(subway)

# # 조세호씨가 몇번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)

# # 정현돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)

# #지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)

# print(subway.pop())
# print(subway)

# 리스트 합치기
num_list = [1,4,2,3,5]
mix_list = ["조세호", 10, True]

num_list.extend(mix_list)
print(num_list)