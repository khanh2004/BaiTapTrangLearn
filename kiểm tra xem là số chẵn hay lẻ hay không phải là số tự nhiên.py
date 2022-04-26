while True:
    a = float(input("nhập vào một số bất kì..."))
    if a % 2 == 0:
        print(f'{a} là số chẵn.')
    elif a % 2 == 1:
        print(f'{a} là số lẻ.')
    else:   
        print(f'{a} không phải số tự nhiên')