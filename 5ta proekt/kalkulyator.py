sorov="ha"
while sorov == "ha":
    num1 = int(input("Birinchi sonni kiriting = "))
    num2 = int(input("Ikkinchi sonni kiriting = "))
    amal = input("Amalni kiritting : ")
    if amal =="*":
        print(f"{num1} {amal} {num2} = {num1*num2}")
    elif amal =="+":
        print(f"{num1} {amal} {num2} = {num1+num2}")
    elif amal =="/":
        print(f"{num1} {amal} {num2} = {num1/num2}")
    elif amal =="-":
        print(f"{num1} {amal} {num2} = {num1-num2}")
    else:
        print(f'{amal} bunday amal topilmadi ⚠ 😕')
    sorov = input("Yana misollar bormi?😀 : ")
    if sorov == "yoq":
        sorov = input("Ok 😉 , \n Yana kerak bo`lsam ha buyrug`ini kiriting : ")
    else:
        if sorov == None:
            print(f"Bu buyrug' topilmadi! {sorov} , ha yoki yoq burug`idan foydalaning")
        else:
            print("buyrug' kiritilmadi")
