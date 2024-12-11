print()


def berekenVerzendkosten(prijs): 
  verzendkosten = 3.95

  if (prijs >= 20):
    verzendkosten = 0

  return verzendkosten


print("Hoe duur is de bestelling?")
winkelmandje = float(input())
verzendkosten = berekenVerzendkosten(winkelmandje)
totaal = winkelmandje + verzendkosten


print("Uw verzendkosten zijn:", verzendkosten)
print(f"Uw totale kosten zijn: {winkelmandje} + {verzendkosten} = {totaal}")


print()