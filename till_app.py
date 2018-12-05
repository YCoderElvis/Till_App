## Till  Program ##

def  main_menu():
    print("************ Main Menu **************")
    print("1.Help")
    print("2.Products in stocks")
    print("3.Quit Program")
    print("*************End of Menu************")

    menu = int(input("Enter a number to navigate program\n"))
    
    if menu ==3:
        print("You have exitted the program")
        
    if menu == 1:
        print("******** ****HELP**************")
        print("This program is a basic till that shows the products sold in Mr.Johnson's shop")
        print("The  software allows you to order two products at a time")
        print("There is  a discount on all products over £50")
        print("At the end of every  transaction, an invoice is printed out")
        print("*********** END  OF  HELP ********")
        return main_menu()
    if menu == 2:
        print("*********PRODUCTS IN STOCKS ************")
        print("a.Ipad Mini --- £250")
        print("b.Macbook Pro --- £2250")
        print("c.Iphone Charger --- £10")
        print("*********END *******************************")
        print("There is discount of 20% for all products over £50")


        product_name = ()

        product = input("Enter a,b or c to navigate products in stocks\n")
        
        ### Products  Section ###

        if product == "c":
            
            ### Iphone Charger ###
            
            product_name = ("Iphone Charger")
            qun_of_charger = int(input("How many of this product are you ordering?\n"))
            price_of_charger = 10
            price_of_charger = qun_of_charger * price_of_charger
            print("The total price for this particular product is ",price_of_charger)
            
            add_more = input("Do you want to order more products?\n")
            
            ### Ask  For  Products to be Added ###

            if add_more == "N":
                  print("************* INVOICE**********")
                  print("Names of Products Ordered : " , product_name)
                  print("Quantity of Iphone Charger : " , qun_of_charger)
                  
                  print("Total Price of Products ordered : " , price_of_charger)
                  print("************** END OF INVOICE ********")
                  
                
            
            if  add_more == "Y":
                print("You can order any of these products : ")
                print("a.Macbook Pro --- £2250")
                print("b.Ipad Mini --- £250")

                add_more_product = input("Enter a or b to navigate products for sales\n")
                if  add_more_product == "a":
                    ### Macbook  Section  within Iphone Charger Section ###
                    
                    product_name = ("Iphone Charger","Macbook Pro")
                    qun_of_mac = int(input("How many of this product are you ordering?\n"))
                    price_of_mac = 2250 
                    price_of_mac = qun_of_mac * price_of_mac
                    print("The total price for this particular product is ",price_of_mac)
                    
                    total_price = price_of_charger + price_of_mac
                    
                    print("************* INVOICE**********")
                    print("Names of Products Ordered : " , product_name)
                    print("Quantity of Iphone Charger : " , qun_of_charger)
                    print("Quantity of Macbook Pro : " , qun_of_mac)
                    print("Total Price of Products ordered : " , total_price)
                    print("************** END OF INVOICE ********")
                    
                if  add_more_product == "b":
                    ### Ipad Mini  Section within Iphone Charger Section ###
                    
                    product_name = ("Iphone Charger","Ipad Mini")
                    qun_of_mini = int(input("How many of this product are you ordering?\n"))
                    price_of_mini = qun_of_mini  * 250
                    print("The total price for this particular product is ",price_of_mini)

                    
                    total_price = price_of_mini + price_of_charger
                    
                    print("************* INVOICE**********")
                    print("Names of Products Ordered : " , product_name)
                    print("Quantity of Iphone Charger : " , qun_of_charger)
                    print("Quantity of Ipad Mini: " , qun_of_mini)
                    print("Total Price of Products ordered : " , total_price)
                    print("************** END OF INVOICE ********")
        

        if product == "b":
             ### Macbook Pro ###
            
            product_name = ("Macbook Pro")
            qun_of_mac = int(input("How many of this product are you ordering?\n"))
            DISCOUNT_PERC = 0.2
            price_of_mac = DISCOUNT_PERC * 2250
            price_of_mac = 2250 - 450
            price_of_mac = qun_of_mac * price_of_mac
            print("The total price for this particular product is ",price_of_mac)
            
            add_more = input("Do you want to order more products?\n")
            
            ### Ask  For  Products to be Added ###

            if add_more == "N":
                  print("************* INVOICE**********")
                  print("Names of Products Ordered : " , product_name)
                  print("Quantity of Macbook Pro : " , qun_of_mac)
                  
                  print("Total Price of Products ordered : " , price_of_mac)
                  print("************** END OF INVOICE ********")
                  
                
            
            if  add_more == "Y":
                print("You can order any of these products : ")
                print("a.Ipad Mini --- £250")
                print("b.Iphone Charger --- £15")

                add_more_product = input("Enter a or b to navigate products for sales\n")
                if  add_more_product == "a":
                    ### Ipad Section  within Macbook Pro Section ###
                    
                    product_name = ("Macbook Pro","Ipad Mini")
                    qun_of_mini = int(input("How many of this product are you ordering?\n"))
                    price_of_mini = DISCOUNT_PERC * 250
                    price_of_mini = 250 - 50
                    price_of_mini = qun_of_mini * price_of_mini
                    print("The total price for this particular product is ",price_of_mini)
                    
                    total_price = price_of_mini + price_of_mac
                    
                    print("************* INVOICE**********")
                    print("Names of Products Ordered : " , product_name)
                    print("Quantity of Ipad Mini : " , qun_of_mini)
                    print("Quantity of Macbook Pro : " , qun_of_mac)
                    print("Total Price of Products ordered : " , total_price)
                    print("************** END OF INVOICE ********")
                    
                if  add_more_product == "b":
                    ### Iphone  Charger  Section within Macbook Pro Section ###
                    
                    product_name = ("Macbook Pro","Iphone Charger")
                    qun_of_charger = int(input("How many of this product are you ordering?\n"))
                    price_of_charger = qun_of_charger  * 15
                    print("The total price for this particular product is ",price_of_charger)

                    
                    total_price = price_of_mac + price_of_charger
                    
                    print("************* INVOICE**********")
                    print("Names of Products Ordered : " , product_name)
                    print("Quantity of Ipad Macbook Pro : " , qun_of_mac)
                    print("Quantity of Iphone Charger: " , qun_of_charger)
                    print("Total Price of Products ordered : " , total_price)
                    print("************** END OF INVOICE ********")
                    
                    


        
        if product == "a":
            
            ### Ipad Mini ###
            
            product_name = ("Ipad Mini")
            qun_of_mini = int(input("How many of this product are you ordering?\n"))
            DISCOUNT_PERC = 0.2
            price_of_mini = DISCOUNT_PERC * 250
            price_of_mini = 250 - 50
            price_of_mini = qun_of_mini * price_of_mini
            print("The total price for this particular product is ",price_of_mini)
            
            add_more = input("Do you want to order more products?\n")
            
            ### Ask  For  Products to be Added ###

            if add_more == "N":
                  print("************* INVOICE**********")
                  print("Names of Products Ordered : " , product_name)
                  print("Quantity of Ipad Mini : " , qun_of_mini)
                  
                  print("Total Price of Products ordered : " , price_of_mini)
                  print("************** END OF INVOICE ********")
                  
                
            
            if  add_more == "Y":
                print("You can order any of these products : ")
                print("a.Macbook Pro --- £2250")
                print("b.Iphone Charger --- £15")

                add_more_product = input("Enter a or b to navigate products for sales\n")
                if  add_more_product == "a":
                    ### Macbook  Section  within Ipad Mini Section ###
                    
                    product_name = ("Ipad Mini","Macbook Pro")
                    qun_of_mac = int(input("How many of this product are you ordering?\n"))
                    price_of_mac = DISCOUNT_PERC * 2250
                    price_of_mac = 2250 - 450
                    price_of_mac = qun_of_mac * price_of_mac
                    print("The total price for this particular product is ",price_of_mac)
                    
                    total_price = price_of_mini + price_of_mac
                    
                    print("************* INVOICE**********")
                    print("Names of Products Ordered : " , product_name)
                    print("Quantity of Ipad Mini : " , qun_of_mini)
                    print("Quantity of Macbook Pro : " , qun_of_mac)
                    print("Total Price of Products ordered : " , total_price)
                    print("************** END OF INVOICE ********")
                    
                if  add_more_product == "b":
                    ### Iphone  Charger  Section within Ipad Mini Section ###
                    
                    product_name = ("Ipad Mini","Iphone Charger")
                    qun_of_charger = int(input("How many of this product are you ordering?\n"))
                    price_of_charger = qun_of_charger  * 15
                    print("The total price for this particular product is ",price_of_charger)

                    
                    total_price = price_of_mini + price_of_charger
                    
                    print("************* INVOICE**********")
                    print("Names of Products Ordered : " , product_name)
                    print("Quantity of Ipad Mini : " , qun_of_mini)
                    print("Quantity of Iphone Charger: " , qun_of_charger)
                    print("Total Price of Products ordered : " , total_price)
                    print("************** END OF INVOICE ********")
                    
                    

