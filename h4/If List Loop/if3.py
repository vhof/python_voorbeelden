from datetime import datetime

maandag = 0
dinsdag = 1
woensdag = 2
donderdag = 3
vrijdag = 4
zaterdag = 5
zondag = 6

vandaag = datetime.today().weekday()

if (vandaag == maandag): 
    print("Maandag!")
elif (vandaag == dinsdag): 
    print("Dinsdag!")
elif (vandaag == woensdag): 
    print("Woensdag!")
elif (vandaag == donderdag): 
    print("Donderdag!")
elif (vandaag == vrijdag): 
    print("Vrijdag!")
elif (vandaag == zaterdag): 
    print("Zaterdag!")
elif (vandaag == zondag): 
    print("Zondag!")

print()