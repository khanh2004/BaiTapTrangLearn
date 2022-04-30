dau_vao = input("nhập hai số cách nhau bởi dấu phẩy...")
tach_chuoi = dau_vao.split(",")
so_dau, so_cuoi = int(tach_chuoi[0]), int(tach_chuoi[1])
for item in range(so_dau , so_cuoi+1) :
    if item % 3 == 0 and item % 5 ==0 :
        print("FizzBuzz")
    elif item % 3 == 0 :
        print("Fizz")
    elif item % 5 ==0 :
        print("Buzz")
    else:
        print(item)