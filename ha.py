import random

pole1 = []
pole2 = []

def nahodny_pocet (prv):
    global pole1
    global pole2
    for i in range(random.randint(1,10)):
        pole1.append(random.randint(1,20))
        pole1.sort
    for a in range(random.randint(1,10)):
        pole2.append(random.randint(1,20))
        pole2.sort

nahodny_pocet()

if len(pole1) > len(pole2):
    print ("První pole má větši delku!")
elif len(pole1) == len(pole2):
    print("Mají stejnou delku!")
else:
    print ("Druhe pole má větší delku!")
print(f"\nDelka prvního pole - {pole1}")
print(f"Delka druhého pole - {pole2}")