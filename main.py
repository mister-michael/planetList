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
   ("Wohlie", "Venus"),
   ("Ricky", "Neptune"),
   ("Jerry", "Neptune"),
   ("Larry", "Neptune"),
]
for planet in planet_list:
    has_visited = False
    a = f'{planet} was visited by '
    b = f'{planet} was not visited by a satelite.'
    
    for el in spacecraft:

        if el[1] == planet:
           a += f'{el[0]}, '
           has_visited = True
    else: 
        a = a[slice(-2)] + f'.'

    if has_visited: 
        print(a)
    else: 
        print(b)
