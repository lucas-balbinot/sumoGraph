import sumolib
import argparse

def get_filepath():
    # parses the input
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--path', 
        '-p', 
        type=str, 
        required=True, 
        action="store", 
        dest="net_file",
        help="The path of the file to be parsed (necessary)"
    )

    # returns the path given
    net_file = parser.parse_args().net_file
    if not net_file:
        parser.print_help()
        quit()
    return net_file

def main():
    # opens the file that will store the connections
    with open('networkConnections.txt', 'w') as w_file:

        # gets the path 
        net_path = get_filepath()

        # reads the network
        network = sumolib.net.readNet(net_path)

        # for every edge in the network
        for edge in network.getEdges():
            # get the nodes that are connected 
            node_from = edge.getFromNode().getID()
            node_to = edge.getToNode().getID()
            
            # and write in the file
            w_file.write(f'{node_from} {node_to}\n')
            


if __name__ == "__main__":
    main()
