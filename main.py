# main.py accessing admin user credential 

from admin_user import ShrisKitchen
try:
    def main() -> object:
        obj = ShrisKitchen("ShrisKitchen")
        print("*" * 30, "WELCOME TO", obj.shris_kitchen_name, "VEG RESTAURANT", "*" * 30, "\n")
        print("-" * 89)
        print("\nHello! Welcome to ShrisKitchen Veg Restaurant, Food Ordering App and Have a 'Good Times' :)\n")
        while True:
            print("-" * 40 + "HOME PAGE" + "-" * 40 + "\n")
            print("\t1. ADMIN \n\t2. USER\n\t3. EXIT\n")
            x = input()
            if x == "1":
                while True:
                    print("\n" + "-" * 40 + "ADMIN PAGE" + "-" * 40 + "\n")
                    print("\t1. ADMIN REGISTRATION\n\t2. ADMIN LOGIN\n\t3. GO BACK\n")
                    y = input()
                    if y == "1":
                        obj.admin_register()
                    elif y == "2":
                        obj.admin_login()
                    elif y == "3":
                        break
                    else:
                        print("\nNOT A VALID OPTION\n")

            elif x == "2":
                while True:
                    print("\n" + "-" * 40 + "USER PAGE" + "-" * 40 + "\n")
                    print("\t1. REGISTER ACCOUNT\n\t2. LOGIN\n\t3. GO BACK\n")
                    y = input()
                    if y == "1":
                        obj.user_register()
                    elif y == "2":
                        obj.user_login()
                    elif y == "3":
                        break
                    else:
                        print("\nNOT A VALID OPTION ")
            elif x == "3":
                break
            else:
                print("NOT A VALID OPTION")

except Exception as e:
    print(e)
    print("SOMETHING GONE WRONG PLEASE TRY AGAIN LATER")

# calling the main function

if __name__ == '__main__':
    main()

print("\nTHANK YOU HAVE A WONDERFULL DAY FROM ShrisKitchen\n")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
