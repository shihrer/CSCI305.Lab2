# TODO: Task 2 - Determine whether two inputs are directly connected
# TODO: Task 3 - Determine whether there is a k-hop connection between two inputs.  Print one solution.  k <= d
# TODO: Task 4 - Determine whether or not there is a connection between two inputs.  Print one solution.

import networkx as nx
import re

import sys


class Lab_2:
    def __init__(self, file_name):
        self.city_nodes = []
        self.graph = nx.Graph()
        self.build_structure(file_name)

    def start_lab(self):
        self.menu()

    def build_structure(self, file_name):
        """
        :param file_name: Name of file to build graph from.
        Builds the graph from a given file name.
        """
        for edge in self.read_file(file_name):
            self.graph.add_edge(edge[0],edge[1],weight=edge[2])

    @staticmethod
    def read_file(file):
        """
        Creates a generator for reading a file line by line.
        :param file: Name of file to open.
        :return: Three tuple (Origin, Destination, Miles) from file
        """
        with open(file, "r") as the_file:
            for line in the_file:
                line = line.strip().lower()
                if line != "" and not re.match("--+|from\s+to\s+miles", line):
                    result = re.split("\s\s+", line)
                    yield result[0], result[1], int(result[2])

    def task1(self, city):
        """
        Find the number of cities directly connected to a given city.
        :param city:
        :return:
        """
        city_neighbors = self.graph.neighbors(city.lower())
        return "{} has {} connections.".format(city, len(city_neighbors))

    def task2(self, source, destination):
        """
        :return: Yes/No string
        Determine if there is a direct connection between two cities.
        """

        if destination in self.graph.neighbors(source):
            return "YES"
        else:
            return "NO"

    def task3(self, source, destination, d):
        """
        :param source: source city string
        :param destination: destination city string
        :param d: Integer for d-hop
        :return: Yes/No string and solution
        Determine if there is a k-hop connection between two cities.
        """

        try:
            path = nx.shortest_path(self.graph, source, destination)
            k = len(path) - 1

            if k <= d:
                return "YES\nd-hops: {}\n{}".format(k, path)
            else:
                return "NO"

        except nx.NetworkXNoPath:
            return "NO"

    def task4(self, source, destination):
        """
        :param source: source city string
        :param destination: destination city string
        :return: Yes/No string and solution
        """

        try:
            path = nx.shortest_path(self.graph, source, destination,weight="weight")
            total_distance = self.get_distance(path)
            return "YES\n{}\nDistance: {}".format(path, total_distance)
        except nx.NetworkXNoPath:
            return "NO"

    def get_distance(self,path):
        total = 0
        for i in range(0, len(path) - 1):
            total += self.graph.get_edge_data(path[i],path[i+1])["weight"]

        return total

    def menu(self):
        while True:
            print("To find the number of cities connected to a city, enter '1'")  # task 1
            print("To find out whether or not there is a direct connection between two cities, enter '2'")  # task 2
            print("To determine whether or not there is a certain length connection between two cities, enter '3'")  # task 3
            print("To find out if there is a connection between two cities, enter '4'")  # task 4
            print("To exit, enter 'e'") # Exit program
            print()
            choice = input("Enter your choice (1, 2, 3, 4, or e) > ")
            print()

            if choice == '1':
                self.task1(input("Enter a city > "))
                print()
            elif choice == '2':
                source = input("Enter a source city > ")
                destination = input("Enter a destination city > ")
                print(self.task2(source.lower(),destination.lower()))
                print()
            elif choice == '3':
                source = input("Enter a source city > ")
                destination = input("Enter a destination city > ")

                valid_input = False
                while not valid_input:
                    int_input = input("Enter a d-hop > ")
                    valid_input = self.is_valid_input(int_input)

                print(self.task3(source, destination, int(int_input)))
            elif choice == '4':
                source = input("Enter a source city > ")
                destination = input("Enter a destination city > ")

                print(self.task4(source, destination))
            elif choice.lower() == 'e':
                sys.exit()
            else:
                print("That is not a valid choice. Please pick again from 1, 2, 3, 4, or e.")
                print()

    @staticmethod
    def is_valid_input(test_input):
        try:
            int(test_input)
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    the_lab = Lab_2("city1.txt")
    the_lab.start_lab()





