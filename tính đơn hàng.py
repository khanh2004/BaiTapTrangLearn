price = float(input("bạn đã mua bao nhiêu tiền hàng?..."))
if price >= 150:
    print("tổng cộng ", price - 50 )
elif price >= 100:
    print("tổng cộng", price - 25)
elif price >= 75:
    print("tổng cộng", price - 15)
else:
    print(f"tổng cộng {price}")