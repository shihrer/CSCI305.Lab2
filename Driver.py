# TODO: Import data set - use dictionary to store already inserted nodes.  Search dictionary before creating new node.  Create new node when there isn't a match.
# TODO: Create command line menu with 4 options (one for each task).
# TODO: Task 1 - Query number of cities directly connected to input
# TODO: Task 2 - Determine whether two inputs are directly connected
# TODO: Task 3 - Determine whether there is a k-hop connection between two inputs.  Print one solution.  k <= d
# TODO: Task 4 - Determine whether or not there is a connection between two inputs.  Print one solution.


class Lab_2:
    def __init__(self, file_name):
        self.build_structure(file_name)
        self.city_nodes = []

    def start_lab(self):
        self.menu()

    def build_structure(self, file_name):
        city_file = open(file_name, "r")

        print(city_file.read())

    def task1(self):
        city = input("Enter a city > ")
        connections = str(len(d[city]))  # 'd' is the dict. Change the name to whatever you want
        print("%s has %s connections.") % (city, connections)

    def task2(self):
        return 0

    def task3(self):
        return 0

    def task4(self):
        return 0

    def store_cities(f):
        for line in f:
            if line.startswith('' or 'from' or '-'):
                line = ''
        # All this does is remove the extra lines. I'm not sure how you want to get and store the rest of the data.


    # Displays menu
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


class City_Node:
    def __init__(self, city_name):
        self.city = city_name
        self.edges = []

    def add_edge(self, connected_node, weight):
        self.edges.add((connected_node, weight))

if __name__ == "__main__":
    the_lab = Lab_2("city1.txt")
    the_lab.start_lab()





