print()


# Alleen cijfers tussen de 1.0 en 10.0 zijn geldig
def vraagCijfer():
  cijfer = float(input("Voer het cijfer in: "))

  while cijfer < 1.0 or cijfer > 10.0:
    print("Dat is geen geldig schoolcijfer!")
    cijfer = float(input("Voer het opnieuw in: "))

  return cijfer


cijfer1 = vraagCijfer()
cijfer2 = vraagCijfer()


print()