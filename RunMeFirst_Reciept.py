import ClothingLine

while True:
    info = str("\nAddress: \nPhone Number:")
    print("\n__________________________Meiple Tree______________________________\n")
    print('We Would like to ask our valued customer to enter the following: \n' + str(info))
    frstname = str(input("Hello customer how can we address you? [Full name]: "))
    Address = str(input("Where is your current Address?: "))
    while True:
        PhnNumber = int(input("What is your current phone number? [+63]: "))
        if PhnNumber > 9999999999 or PhnNumber < 999999999:
            print('please enter a correct phone number')
        else:
            break
    print("\n____________________________________________________________________\n")
       
    print("\n__________________________Meiple Tree______________________________\n")
    print(f"Address: {Address}")
    print(f"Phone Number: +63{PhnNumber}")
    print(f"Full Name: {frstname}")
    print()
    informationresult = str(input('Is the information presented above correct? [Y/N] :'))
    if informationresult.lower() == "y":
        print()
        while True:    
            print("\n__________________________Meiple Tree______________________________\n")
            if ClothingLine.jackets_cart:
                for item in ClothingLine.jackets_cart:
                    print(f"{item}\n")
            if ClothingLine.shirts_cart:
                for item in ClothingLine.shirts_cart:
                    print(f"{item}\n")
            if ClothingLine.pants_cart:
                for item in ClothingLine.pants_cart:
                    print(f"{item}\n")
            if ClothingLine.hats_cart:
                for item in ClothingLine.hats_cart:
                    print(f"{item}\n")
            print("\n____________________________________________________________________\n")
            with open('Resibo.txt', 'r') as f:
                f_contents = f.write()
                print(f_contents)
            break
        break
    if informationresult.lower() == "n":
        print("Kindly Double Check the information")
    else:
        print("Invalid Response, Try Again")
        