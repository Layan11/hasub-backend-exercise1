"""
The load balancing algorithm i chose to implement in the round robin, the load balancer goes over all the servers
in a circular way, and each server that can take a request and is not full the load balancer gives adds the request to
that server, otherwise it continues to check another server.

The data consistency strategy i chose is strong consistency, the downside is that it slows down the process of buying
tickets because the operation has to stop whenever someone is buying a ticket, so it slows down everything and people
may have to wait a lot to buy a ticket. The upside is that the data is always consistent so we wouldn't have the case of
two people buying the same ticket at the same time.
I chose string consistency because it is important to not let someone think they bought a ticket they want and then
being told that someone else has already bought the same ticket and that the system made a mistake because the data base
wasn't updated.

So the flow of this is: whenever someone buys a ticket, all the servers stop and don't accept any buy requests, until
all databases are updated with the last sale.
"""


class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.requests = []

    # round robin load balancing
    def send_request_to_server(self):
        for server in self.servers:
            if len(server.requests) < server.max_requests:
                server.requests.append(self.requests[0])
                self.requests.pop()

    # keep listening for requests and when recieved add request to the list of requests
    # and use the send_request_to_server method
    def recieve_request(self, request):
        self.requests.append(request)
        self.send_request_to_server()

