#  Hint:  You may not need all of these.  Remove the unused functions.


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    #initialize dictionary
    ticket_dict = {}
    #create list of nones in the proper length
    route = [None] * (len(tickets))
    #iterate over tickets list
    for ticket in tickets:
        # if ticket sorce is none move to head of route list this is the starting location
        if ticket.source == "NONE":
            route[0] = ticket.destination
        #add not none tickets to ticket dict
        ticket_dict[ticket.source] = ticket.destination
    # add ticket dict k/v to route
    for i in range(1, len(tickets)):
        route[i] = ticket_dict[route[i-1]]
    # return route
    return route
