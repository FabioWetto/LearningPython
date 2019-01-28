from airtravel import make_flight
from pprint import pprint

print("Progettino di esercizio con Python!")

f = make_flight()

print(f)

print(f.number())

print(f.aircraft_model())

pprint(f._seating)

f.relocate_passenger("4B", "13B")

pprint(f._seating)

print("Sono rimasti disponibili {} posti".format(f.num_available_seats()))
