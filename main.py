planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

last_two_planets = ["Uranus", "Neptune"]
planet_list.extend(last_two_planets)

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

planet_list.append("Pluto")

rocky_planets = slice(0,4)

del planet_list[-1]

print("planet list", planet_list)
print("rocky planets", planet_list[rocky_planets])

spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
]

for planet in planet_list:
    has_been_visited = ""
    craft = ""
    for el in spacecraft:
        if el[1] == planet:
            has_been_visited = True
            craft = el[0]
    if has_been_visited == True:
        print(f"{planet} has been visited by {craft}")
    else:
        print(f"{planet} has not been visited by a satelite.")


