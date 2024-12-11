from datetime import datetime

dagen = ["Maandag", "Dinsdag", "Woensdag", "Donderdag", 
         "Vrijdag", "Zaterdag", "Zondag"]


dagNummer = datetime.today().weekday()
vandaag = dagen[dagNummer]


print(vandaag)
print()