# site_name = "http://kcg.go.kr"
while(1) :
    site_name = input()
    print(site_name)

    find_comma = site_name.find(".")

    site_name = site_name.replace("http://", "")
    site_name = site_name[:find_comma]

    password = site_name[:3] + str(len(site_name)) + str(site_name.count("e")) + "!"

    print("{0}의 비밀번호는 {1}입니다.".format(site_name,password))