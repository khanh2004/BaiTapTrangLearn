while True:
    weight = float(input("your weight in kg..."))
    height = float(input("your height in m..."))
    BMI = weight/(height*height)
    if BMI > 40:
        print("BMI = {BMI}>>> béo phì cấp độ 3 ")
    elif 35 <= BMI < 40:
        print(f"BMI = {BMI}>>> béo phì cấp độ 2")
    elif 30 <= BMI < 35:
        print(f"BMI = {BMI}>>> béo phì cấp độ 1")
    elif 25 <= BMI < 30: 
        print(f"BMI = {BMI}>>> thừa cân")
    elif 18.5 <= BMI < 25:
        print(f"BMI = {BMI}>>> bình thường")
    elif 17<= BMI < 18.5:
        print(f"BMI = {BMI}>>> gầy cấp độ 1")
    elif 16 <= BMI < 17: 
        print(f"BMI = {BMI}>>> gầy cấp độ 2")
    else:
        print(f"BMI = {BMI}>>> gầy cấp độ 3")