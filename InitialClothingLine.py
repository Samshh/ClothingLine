print("Welcome to _______")
# S or Q
size_cart = []
while True:
    control = str(input("S = start, Q = quit:"))
    if control == "S":
        # size
        while True:
            size = str(input("Enter size:"))
            if size == "small":
                print("you have selected small")
                break
            elif size == "medium":
                print("you have selected medium")
                break
            elif size == "large":
                print("you have selected large")
                break
            else:
                print("enter only, small, medium. or large!")
            size_cart.append(size)
        
        # thrift preference
        while True:
            thrift_preference = str(input("are you interested in selecting your thrift preference?:"))
            if thrift_preference == "yes":
                
                # clothing line
                while True:
                    clothing_line = str(input("select either shirts, jackets, pants, or hats:"))
                    if clothing_line == "shirts":
                        
                        # shirts
                        while True:
                            shirts = str(input("select either graphic, plain, or polo:"))
                            if shirts == "graphic":
                                print("graphic shirts cost 400 pesos")
                                break
                            elif shirts == "plain":
                                print("plain shirts cost 300 pesos")
                                break
                            elif shirts == "polo":
                                print("polo shirts cost 500 pesos")
                                break
                            else:
                                print("")
                        break
                    
                    elif clothing_line == "jackets":
                        
                        # jackets
                        while True:
                            jackets = str(input("select either varsity, plain, bomber, or flannel:"))
                            if jackets == "varsity":
                                print("varsity jackets cost 450 pesos")
                                break
                            elif jackets == "plain":
                                print("plain jackets cost 400 pesos")
                                break
                            elif jackets == "bomber":
                                print("bomber jackets cost 500 pesos")
                                break
                            elif jackets == "flannel":
                                print("flannel jackets cost 600 pesos")
                            else:
                                print("")
                        break
                    
                    elif clothing_line == "pants":
                        
                        # pants
                        while True:
                            pants = str(input("select either denim, cargo, wide, or ankle:"))
                            if pants == "denim":
                                print("denim pants cost 500 pesos")
                                break
                            elif pants == "cargo":
                                print("cargo pants cost 450 pesos")
                                break
                            elif pants == "wide":
                                print("wide pants cost 500 pesos")
                                break
                            elif pants == "ankle":
                                print("ankle pants cost 400 pesos")
                            else:
                                print("")
                        break
                    
                    elif clothing_line == "hats":
                        
                        # hats
                        while True:
                            hats = str(input("select either branded, beanie, or bucket:"))
                            if hats == "branded":
                                print("branded hats cost 200 pesos")
                                break
                            elif hats == "beanie":
                                print("beanie hats cost 300 pesos")
                                break
                            elif hats == "bucket":
                                print("bucket hats cost 300 pesos")
                                break
                            else:
                                print("")
                        break
                    
                    else:
                        print("")
                break
            else:
                if thrift_preference == "no":
                    print("Bye-bye...")
                    break
                else:
                    print("")
    else:
        if control == "Q":
            print("Quit...")
            break
        else:
            print("input either S or Q only!")