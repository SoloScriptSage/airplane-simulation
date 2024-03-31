# Airport Simulator Project
# Hirchuk Vladyslav

import random
from plane import Plane
from time import *

def simulate_arrival(arrivals_queue):
    plane = Plane()
    print(f"Arriving: {plane}")
    arrivals_queue.append(plane)

def simulate_landing(arrivals_queue, terminals):
    if arrivals_queue and len(terminals) < 4:
        landed_plane = arrivals_queue.pop(0)
        terminals.append(landed_plane)
        print(f"Landing: {landed_plane}")

def simulate_takeoff(terminals, departure_queue):
    if terminals: 
        departing_plane = terminals.pop(0)
        departure_queue.append(departing_plane)
        print(f"Taxiing: {departing_plane}")

def simulate_departure(departure_queue, archive):
    if departure_queue:
        departed_plane = departure_queue.pop(0)
        archive.append(departed_plane)
        print(f"Departing: {departed_plane}")

def airport_simulation():
    arrivals_queue = []
    departure_queue = []
    terminals = []
    archive = []

    plane = Plane()

    for i in range(50):
        event = random.randint(0, 3)
        if event == 0:
            simulate_arrival(arrivals_queue)
        elif event == 1:
            simulate_landing(arrivals_queue, terminals)
        elif event == 2: 
            simulate_takeoff(terminals, departure_queue)
        elif event == 3:
            simulate_departure(departure_queue, archive)

        sleep(0.1)

    return archive

def print_report(planes):
    print("\nReport of Departed Airplanes:")
    print("+----+--------------------------------+------------------+")
    print("| #  |             Airline            |   Flight Number  |")
    print("+----+--------------------------------+------------------+")

    for i, plane in enumerate(planes, start=1):
        airline_str = plane.airline.ljust(30)
        flight_no_str = f"Flight {plane.flightNo}".ljust(16)
        print(f"| {i}  | {airline_str} | {flight_no_str} |")

    print("+----+--------------------------------+------------------+")

def main():
    visited_planes = airport_simulation()
    print_report(visited_planes)

if __name__ == "__main__":
    main()