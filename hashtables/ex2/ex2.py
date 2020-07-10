#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Create a cache
    routes = {}

    # Iterate through the list of tickets, adding routes into # the cache
    for route in tickets:
        if route not in routes:
            routes[route.source] = route.destination

    # Starting route will be 'NONE'
    starting_souce = routes['NONE']

    # The final list including the starting, to be returned in the end
    stops = [starting_souce]

    # Iterate through the tickets list
    for i in range(length-1):
        next_dest = stops[i]

        # The next stop should be the value of
        # the current source
        next_stop = routes[next_dest]

        # Add our next stop to the list of stops
        stops.append(next_stop)


    return stops
