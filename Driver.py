# TODO: Import data set - use dictionary to store already inserted nodes.  Search dictionary before creating new node.  Create new node when there isn't a match.
# TODO: Create command line menu with 4 options (one for each task).
# TODO: Task 1 - Query number of cities directly connected to input
# TODO: Task 2 - Determine whether two inputs are directly connected
# TODO: Task 3 - Determine whether there is a k-hop connection between two inputs.  Print one solution.  k <= d
# TODO: Task 4 - Determine whether or not there is a connection between two inputs.  Print one solution.

import networkx as nx
import re


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
            self.graph.add_edge(edge[0],edge[1],object=edge[2])

    @staticmethod
    def read_file(file):
        """
        Creates a generator for reading a file line by line.
        :param file: Name of file to open.
        :return: Three tuple (Origin, Destination, Miles)
        """
        with open(file, "r") as the_file:
            for line in the_file:
                line = line.strip().lower()
                if line != "" and not re.match("--+|from\s+to\s+miles", line):
                    result = re.split("\s\s+", line)
                    yield result[0], result[1], int(result[2])

    def task1(self):
        """
        Find the number of cities directly connected to a given city.
        """
        city = input("Enter a city > ")
        city_neighbors = self.graph.neighbors(city.lower())
        print("{} has {} connections.".format(city, len(city_neighbors)))

    def task2(self):
        """
        :return: Yes/No string
        Determine if there is a direct connection between two cities.
        """
        return 0

    def task3(self, d):
        """
        :param d: Integer for d-hop
        :return: Yes/No string and solution
        Determine if there is a k-hop connection between two cities.
        """
        return 0

    def task4(self):
        """

        :return: Yes/No string and solution
        Determine if there is a connection between two cities and output one out.
        """
        return 0

    def menu(self):
        print("To find the number of cities connected to a city, enter '1'")  # task 1
        print("To find out whether or not there is a direct connection between two cities, enter '2'")  # task 2
        print("To determine whether or not there is a certain length connection between two cities, enter '3'")  # task 3
        print("To find out if there is a connection between two cities, enter '4'")  # task 4

        while True:
            choice = input("Enter your choice (1, 2, 3, or 4) > ")
            if choice == '1':
                self.task1()
            elif choice == '2':
                self.task2()
            elif choice == '3':
                self.task3()
            elif choice == '4':
                self.task4()
            else:
                print("That is not a valid choice. Please pick again from 1, 2, 3, or 4.")

if __name__ == "__main__":
    the_lab = Lab_2("city1.txt")
    the_lab.start_lab()





