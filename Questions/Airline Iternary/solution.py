def get_itinerary(flights, starting_point, current_itinerary):

    if not flights:
        return current_itinerary + [starting_point]

    updated_itinerary = None
    for index, (city_1, city_2) in enumerate(flights):
        if starting_point == city_1:
            child_itinerary = get_itinerary(
                flights[:index] + flights[index + 1:], city_2, current_itinerary + [city_1])
            if child_itinerary:
                if not updated_itinerary or "".join(child_itinerary) < "".join(updated_itinerary):
                    updated_itinerary = child_itinerary

    return updated_itinerary


size = int(input())
array_input = []
for x in range(size):
    array_input.append(tuple(input().split()))

g = get_itinerary(array_input,'MSC',[])
print(" ".join(g))
