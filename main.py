from GraphSearch import *


def print_path(array, via=None):
    if len(array) == 3 and not via:
        print(f"Traveling from {array[0]} to {array[-1]} will demand you to travel through {array[-2]}.")
    elif len(array) == 4:
        if via:
            print(
                f"Traveling from {array[0]} to {array[-1]} via {via} will demand you to travel through {array[-3]} and {array[-2]}.")
        else:
            print(
                f"Traveling from {array[0]} to {array[-1]} will demand you to travel through {array[-3]} and {array[-2]}.")


def main():
    flight_graph = {
        "Omaha": ["Chicago", "Dallas", "Houston"],
        "Louisville": ["Dallas", "Houston", "Baltimore", "Chicago"],
        "Baltimore": ["Houston", "Dallas", "Chicago", "Salt Lake City", "Louisville", "Portland"],
        "Portland": ["Chicago", "Baltimore"],
        "Salt Lake City": ["Chicago", "Baltimore", "Dallas", "Houston"],
        "Belize City": ["Houston"],
        "Dallas": ["Omaha", "Louisville", "Baltimore", "Salt Lake City", "Houston", "Chicago"],
        "Houston": ["Chicago", "Omaha", "Dallas", "Louisville", "Baltimore", "Salt Lake City", "Belize City"],
        "Chicago": ["Omaha", "Louisville", "Baltimore", "Portland", "Salt Lake City", "Dallas", "Houston"]
    }

    path_Oma_Sdf = bfs_shortest_path(flight_graph, "Omaha", "Louisville")
    path_Bwi_Slc = bfs_shortest_path(flight_graph, "Baltimore", "Salt Lake City")
    path_Bwi_Pwm = list([path_Bwi_Slc[0]])
    [path_Bwi_Pwm.append(x) for x in bfs_shortest_path(flight_graph, path_Bwi_Slc[-1], "Portland")]
    path_Bze_Pwm = bfs_shortest_path(flight_graph, "Belize City", "Portland")

    print_path(path_Oma_Sdf)
    print_path(path_Bwi_Pwm, "Salt Lake City")
    print_path(path_Bze_Pwm)


if __name__ == '__main__':
    main()
