daily_spending = {"30/04" : {"date" : "30/04", "products" : "apple, banana, toothpast", "cost" : "15$"}, 


                "01/05" : {"date" : "01/05","products" : "iphone 13 promax 128gb, car, toys", "cost" : "200000$"}}

def add_item (daily_spending,new_item) :
        daily_spending.update(new_item)

def del_item (daily_spending, deleted_item_name) :
        number_of_day = len(daily_spending)
        days_counting_variable = 0
        for i in daily_spending.copy() :
            days_counting_variable = days_counting_variable +1
            if i == deleted_item_name :
                while True :
                    print(f"Are you sure to delete {daily_spending[i]} permanently ?")
                    final_choice = input("Enter 'yes' or 'no'...")
                    if final_choice.upper() == "YES":
                        del daily_spending [i]
                        print("successfully deleted")
                        break
                    elif final_choice.upper() == "NO":
                        break
                    elif final_choice.upper != "NO" and "YES":
                        print("Invalid Syntax")

            else:
                print("Date is not found, please try again.")        



while True :        
    print(daily_spending)
    print("what do you want")
    print("1: ADD, 2:DELETE")
    choice = (input("your choice 1 OR 2 ..."))
        
    if choice == "1" :
        added_item_name = input("date...dd/mm...")
        for i in daily_spending.copy() :
            if i == added_item_name :
                    while True:
                        print(f"Date {i} has already existed",end=", ")
                        alternative = input("do you want to change the products and cost? Enter 'yes' or 'no'... ")
                        if alternative.upper() == "NO":
                            break            
                        elif alternative.upper() == "YES":
                            changed_products = input('Enter the products, devided by ","...')
                            changed_cost = input('Enter the final cost, ended by "$"...') 
                            daily_spending[i] ["products"] = changed_products
                            daily_spending[i] ["cost"]     = changed_cost
                            print("successfully changed")
                            break
                                
                                
                    break

            else:             
                products = input("products...")
                cost = input("cost...")
                new_item = {added_item_name : {"date" : added_item_name,"products" : products, "cost" : cost}}
                add_item(daily_spending, new_item)
                print("successfully saved")
                break    
          
     
                

    elif choice == "2" :
        deleted_item_name = input("The date of daily spending day you want to deleted permanently...dd/mm")
        del_item(daily_spending,deleted_item_name)

    else:
        print("Invalid Syntax, please try again.")



