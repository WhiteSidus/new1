import random

pole1 = []
pole2 = []

def nahodny_pocet (prvek,prvek2):

    for i in range(random.randint(1,10)):
        prvek.append(random.randint(1,20))
        prvek.sort()
    for a in range(random.randint(1,10)):
        prvek2.append(random.randint(1,20))
        prvek2.sort()

nahodny_pocet(pole1,pole2)

if len(pole1) > len(pole2):
    print ("První pole má větši delku!")
elif len(pole1) == len(pole2):
    print("Mají stejnou delku!")
else:
    print ("Druhe pole má větší delku!")
print(f"\nDelka prvního pole - {pole1}")
print(f"Delka druhého pole - {pole2}")