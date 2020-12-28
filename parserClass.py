import sumolib
import argparse
import re

class NetParser:
    def __init__(self):
        self.path = self.get_filepath()
        self.fileName = self.get_filename() + '.txt'

    def get_filepath(self):
        # parses the input
        parser = argparse.ArgumentParser()

        parser.add_argument(
            '--path', 
            '-p', 
            type=str, 
            required=True, 
            action="store", 
            dest="net_file",
            help="The path to the file to be parsed (necessary)"
        )

        # returns the path given
        net_file = parser.parse_args().net_file
        if not net_file:
            parser.print_help()
            quit()
        return net_file
    
    def get_filename(self):
        regex_parser = re.compile(r'''
            ([0-9a-zA-Z]*)              #gets the word, not including the '/' of the path if it cointains
            [.]net[.]xml          #the string must end in '.net.xml', but not include it
            $                           #indicates the end of the string
        ''', re.VERBOSE)

        return regex_parser.findall(self.path)[0]

    def main(self):
        # opens the file that will store the connections
        with open(self.fileName, 'w') as w_file:

            # reads the network
            network = sumolib.net.readNet(self.path)

            # for every edge in the network
            for edge in network.getEdges():
                # get the nodes that are connected 
                node_from = edge.getFromNode().getID()
                node_to = edge.getToNode().getID()
                
                # and write in the file
                w_file.write(f'{node_from} {node_to}\n')

NetParser().main()