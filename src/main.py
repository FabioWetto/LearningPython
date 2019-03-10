from airtravel import *
from pprint import pprint
from calculus.linesandpoints import *

scelta = input("Scegli che esercizino lanciare!\n\n1) Modello per voli aerei\n2) Calcolo della distanza fra retta e "
               "punto\nScelta: ")

if scelta == "1":
    print("\nProgettino di esercizio con Python!")

    volo1, volo2 = make_flights()

    print(volo1)

    print(volo1.number())

    print(volo1.aircraft_model())

    pprint(volo1._seating)

    volo1.relocate_passenger("4B", "13B")

    print("Dopo spostamento di un passeggero:")

    pprint(volo1._seating)

    print("Sono rimasti disponibili {} posti".format(volo1.num_available_seats()))

    volo1.make_boarding_cards(console_card_printer)
else:
    result = linesandpoints()
    result.distancepointfromline()
