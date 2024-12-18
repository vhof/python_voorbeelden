ondergrens = int(input("Wat is de ondergrens: "))
bovengrens = int(input("Wat is de bovengrens: "))
geraden = False
 
while not geraden:
    poging = int((bovengrens + ondergrens) / 2)
    print("\nDe computer denkt: " + str(poging))

    antw = input("Is dit goed (g), hoger (h), of lager (l)? ")
    
    if antw == "g":
        print("\nYes, ik heb het geraden!")
        geraden = True

    elif antw == "h":
        ondergrens = poging

    elif antw == "l":
        bovengrens = poging