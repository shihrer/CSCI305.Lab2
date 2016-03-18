"""
CSCI 305
Lab 2

Michael Shihrer
Matthew Wentz

Program Info:

    Python 3.5.1
    Requires the imports re (for regular expression) and networkx (for graphs).
    Install networkx with pip: pip install networkx
    http://pypi.python.org/pypi/networkx
    https://networkx.github.io/documentation/latest/install.html

    if setuptools is not installed, follow instructions:

    https://pypi.python.org/pypi/setuptools
"""

import networkx as nx
import re

import sys


class Lab_2:
    def __init__(self, file_name):
        """
        Simple init method for Lab_2 class.
        :param file_name: String of file name to build graph.
        """
        self.city_nodes = []
        self.graph = nx.Graph()
        self.build_structure(file_name)

    def start_lab(self):
        """
        Start the lab by displaying the menu.
        """
        self.menu()

    def build_structure(self, file_name):
        """
        Builds the graph from a given file name.
        :param file_name: Name of file to build graph from.
        """

        # Loop through each tuple and add them to the graph.
        for edge in self.read_file(file_name):
            self.graph.add_edge(edge[0],edge[1],weight=edge[2])

    @staticmethod
    def read_file(file):
        """
        Creates a generator for reading a file line by line.
        :param file: Name of file to open.
        :return: Three tuple (Origin, Destination, Miles) from file
        """

        # Open the file, read each line, split it into a tuple, and return that.
        with open(file, "r") as the_file:
            for line in the_file:
                line = line.strip().lower()

                # Ignore lines that are blank, just dashes, or the header column.
                if line != "" and not re.match("--+|from\s+to\s+miles", line):
                    result = re.split("\s\s+", line) # regex to split by variable length of whitespace
                    yield result[0], result[1], int(result[2]) # return tuple (source, destination, weight)

    def task1(self, city):
        """
        Find the number of cities directly connected to a given city.
        :param city: string of city name
        :return: string to print for result of task 1
        """

        # Get a list of neighbors.
        try:
            city_neighbors = self.graph.neighbors(city.lower())
            return "{} has {} connections.".format(city, len(city_neighbors))
        except nx.NetworkXError as e:
            return e

    def task2(self, source, destination):
        """
        Determine if there is a direct connection between two cities.
        :param source: Name of source city
        :param destination: Name of destination city
        :return: Yes/No string
        """

        # Just check if destination is in the source's neighbors.
        try:
            if destination in self.graph.neighbors(source):
                return "YES"
            else:
                return "NO"
        except nx.NetworkXError as e:
            return e

    def task3(self, source, destination, d):
        """
        Determine if there is a k-hop connection between two cities.
        :param source: source city string
        :param destination: destination city string
        :param d: Integer for d-hop
        :return: Yes/No string and path solution
        """

        try:
            # Shortest path is by length of nodes.  If shortest path isn't <= d, no path will be.
            path = nx.shortest_path(self.graph, source, destination)
            k = len(path) - 1 # compute K

            if k <= d: # Compare K and D
                return "YES\nd-hops: {}\n{}".format(k, path)
            else:
                return "NO"
        # This exception is thrown when there are no paths.  This is a "NO"
        except nx.NetworkXNoPath:
            return "NO"
        except nx.NetworkXError as e:
            return e

    def task4(self, source, destination):
        """
        Determine if there is a path between two cities.  Output path and total distance.
        :param source: source city string
        :param destination: destination city string
        :return: Yes/No string and solution
        """

        try:
            # Just find the shortest path.
            path = nx.shortest_path(self.graph, source, destination,weight="weight")
            total_distance = self.get_distance(path)
            return "YES\n{}\nDistance: {}".format(path, total_distance)
        # If there are no paths, say "NO"
        except nx.NetworkXNoPath:
            return "NO"
        except nx.NetworkXError as e:
            return e
        except KeyError:
            return "The node {} is not in the graph.".format(source)

    def get_distance(self,path):
        """
        Gets total distance in a path from the graph.
        :param path:
        :return:
        """
        total = 0
        # Loop through the path, look up the weight of each edge, and add that to the total.
        for i in range(0, len(path) - 1):
            total += self.graph[path[i]][path[i+1]]["weight"]

        return total

    def menu(self):
        """
        This displays the menu.
        """
        while True:
            print("To find the number of cities connected to a city, enter '1'")  # task 1
            print("To find out whether or not there is a direct connection between two cities, enter '2'")  # task 2
            print("To determine whether or not there is a certain length connection between two cities, enter '3'")  # task 3
            print("To find out if there is a connection between two cities, enter '4'")  # task 4
            print("To exit, enter 'e'") # Exit program
            print()
            choice = input("Enter your choice (1, 2, 3, 4, or e) > ")
            print()

            if choice == '1': # Call task 1
                print(self.task1(input("Enter a city > ")))
                print()
            elif choice == '2': # Call task 2
                source = input("Enter a source city > ")
                destination = input("Enter a destination city > ")
                print(self.task2(source.lower(),destination.lower()))
                print()
            elif choice == '3': # Call task 3
                source = input("Enter a source city > ")
                destination = input("Enter a destination city > ")

                # Keep asking until valid input is entered.
                valid_input = False
                while not valid_input:
                    int_input = input("Enter a d-hop > ")
                    valid_input = self.is_valid_input(int_input)

                print(self.task3(source, destination, int(int_input)))
                print()
            elif choice == '4': # Call task 4
                source = input("Enter a source city > ")
                destination = input("Enter a destination city > ")

                print(self.task4(source, destination))
                print()
            elif choice.lower() == 'e': # Exit the program
                sys.exit()
            else: # User needs to supply valid input.
                print("That is not a valid choice. Please pick again from 1, 2, 3, 4, or e.")
                print()

    @staticmethod
    def is_valid_input(test_input):
        """
        Test if an input can be casted to int.
        :param test_input: any input to be tested
        :return: True/False depending on if input can be cast.
        """

        # Just attempt to cast the input.
        try:
            int(test_input)
            return True
        except ValueError:
            return False

# Runs the code.
if __name__ == "__main__":
    the_lab = Lab_2("city1.txt")
    the_lab.start_lab()
