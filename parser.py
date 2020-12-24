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

    # returns the file path given 
    return parser.parse_args().net_file


def main():
    # opens the file that will store the connections
    with open('networkconnections.txt', 'w') as w_file:

        # gets the path given to the program
        net_path = get_filepath()

        assert net_path != -1, "Error in the file path"

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

