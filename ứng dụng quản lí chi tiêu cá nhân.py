danh_sach_mon_an = {"30/04" : {"date" : "30/04", "products" : "apple, banana, toothpast", "cost" : "15$"}, 


                "01/05" : {"date" : "01/05","products" : "iphone 13 promax 128gb, car, toys", "cost" : "200000$"}}

def them_mon (danh_sach_mon_an,them_mon_moi) :
        danh_sach_mon_an.append(them_mon_moi)

def xoa_mon (danh_sach_mon_an, mon_can_xoa) :
        tong_so_mon_an = len(danh_sach_mon_an)
        dishes_counting_variable = 0
        for i in danh_sach_mon_an.copy() :
            dishes_counting_variable = dishes_counting_variable +1
            if i == mon_can_xoa :
                while True :
                    print(f"Are you sure to delete {danh_sach_mon_an[i]} permanently ?")
                    final_choice = input("Enter 'yes' or 'no'...")
                    if final_choice.upper() == "YES":
                        del danh_sach_mon_an [i]
                        print("successfully deleted")
                        break
                    elif final_choice.upper() == "NO":
                        break
                    elif final_choice.upper != "NO" and "YES":
                        print("Invalid Syntax")

            elif dishes_counting_variable == tong_so_mon_an :
                print("Date is not found, please try again.")        



while True :        
    print(danh_sach_mon_an)
    print("what do you want")
    print("1: ADD, 2:DELETE")
    choice = (input("your choice 1 OR 2 ..."))
        
    if choice == "1" :
        added_item_name = input("date...dd/mm...")
        for i in danh_sach_mon_an.copy() :
            if i == added_item_name :
                    while True:
                        print(f"Date {i} has already existed",end=", ")
                        alternative = input("do you want to change the products and cost? Enter 'yes' or 'no'... ")
                        if alternative.upper() == "NO":
                            break            
                        elif alternative.upper() == "YES":
                            changed_products = input('Enter the products, devided by ","...')
                            changed_cost = input('Enter the final cost, ended by "$"...') 
                            danh_sach_mon_an[i] ["products"] = changed_products
                            danh_sach_mon_an[i] ["cost"]     = changed_cost
                            print("successfully changed")
                            break
                                
                                
                    break

            else:             
                products = input("products...")
                cost = input("cost...")
                new_item = {added_item_name : {"date" : added_item_name,"products" : products, "cost" : cost}}
                add_item(danh_sach_mon_an, new_item)
                print("successfully saved")
                break    
          
     
                

    elif choice == "2" :
        mon_can_xoa = input("The date of daily spending day you want to deleted permanently...dd/mm or enter 'exit' if you want to return...")
        del_item(danh_sach_mon_an,mon_can_xoa)

    else:
        print("Invalid Syntax, please try again.")
