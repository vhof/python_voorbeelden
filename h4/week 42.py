# variabele 

aantal = 500

# Printen van tekst
# Let op: De te printen tekst zet je tussen dubbele qoutes
print("aantal")

# Printen van een variabele
# Geen dubbele qoutes gebruiken
print(aantal)

# Printen van tekst + variabele
# Python kan geen tekst en numeriek in 1 regel printen.
# Daarom de inhoud van variabele aantal (is integer) omzetten naar tekst. 
# Mbv functie str()
print("aantal is:" + str(aantal))

# Let op :
# Pyhton gebruikt het + teken op twee manieren.
# In het voorbeeld hiervoor werd het gebruikt om twee stukken aan elkaar te plakken (concateneren)
# In het voorbeeld hierna wordt het gebruikt als wiskundige bewerking. 
print(3+5)

# Gebruik formatted print
print(f"aantal is: {aantal}")

