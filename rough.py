class Graph:
    # Consructor 
    def __init__(self):
        self.graph = {}

    def addCity(self, city):
        if city not in self.graph:
            self.graph[city] = []

    def addFlight(self, city1, city2):
        if city1 in self.graph and city2 in self.graph:
            self.graph[city1].append(city2)
            self.graph[city2].append(city1)

    def displayFlights(self):
        for city, connections in self.graph.items():
            print(f"From {city} to {" and " .join(connections)} ")


if __name__ == "__main__":
    citiesGraph = Graph()

    # Cities List
    cityList = ["Seattle", "San Francisco", "Los Angeles", "Denver",
                        "Kansas City", "Dallas", "Houston", "Chicago", "Boston",
                        "New York", "Atlanta", "Miami"]
    # Add cities in a dictionary as a key(nodes)
    for city in cityList:
        citiesGraph.addCity(city)

    availableFlights = [
        ("Seattle", "San Francisco"), ("Seattle", "Denver"), ("San Francisco", "Denver"), ("San Francisco", "Los Angeles"),
        ("Los Angeles", "Dallas"), ("Denver", "Chicago"), ("Denver", "Kansas City"), ("Kansas City", "Chicago"),
        ("Kansas City", "New York"), ("Kansas City", "Atlanta"), ("Kansas City", "Dallas"), ("Chicago", "Boston"),
        ("Chicago", "New York"), ("Dallas", "Atlanta"), ("Dallas", "Houston"), ("Atlanta", "Miami")
    ]

    # Add available flights as value of the key(edges)
    for city1, city2 in availableFlights:
        citiesGraph.addFlight(city1, city2)

    # Display Available Flights
    citiesGraph.displayFlights()