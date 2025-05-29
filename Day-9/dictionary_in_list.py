travel_log=[
    {
        "contry": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "contry": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# travel_log += [{"contry": "Russia", "visits": 2, "cities": ["Moscow", "Saint Perersberg"]}]

def add_new_contry(contry_visited, times_visted, cities_name):
    new_country ={}
    new_country["country"] = contry_visited
    new_country["visisits"] = times_visted
    new_country["cities"] = cities_name
    travel_log.append(new_country)

# I tried this code like this but is not effective
    travel_log.append({contry_visited, times_visted, cities_name})

add_new_contry()

print(travel_log)

# {}