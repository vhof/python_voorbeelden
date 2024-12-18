import math

# Een functie om de letters a, b, en c te vragen.
def vraagLetter(letter):
    waarde = input("Welke waarde heeft: " + letter + "? ")
    return waarde


# Een functie om de discriminant te berekenen
def berekenD(a, b, c):
    return (b ** 2) - (4 * a * c)


# De functie om x1 te berekenen
def berekenX1(a, b, c, d):
    return (-b - math.sqrt(d)) / (2 * a)


# De functie om x2 te berekenen
def berekenX2(a, b, c, d):
    return (-b + math.sqrt(d)) / (2 * a)



# Hoofdprogramma

print("De ABC-formule!")

# Vraag de waarden voor a, b en c
a = float(vraagLetter("a"))
b = float(vraagLetter("b"))
c = float(vraagLetter("c"))

# Bereken de discriminant
d = berekenD(a, b, c)
print("D: " + str(d))

# Bereken x1 en x2 en geef deze waarden weer
x1 = round(berekenX1(a, b, c, d), 1)
x2 = round(berekenX2(a, b, c, d), 1)

print("x1: " + str(x1))
print("x2: " + str(x2))