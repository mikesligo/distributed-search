__author__ = 'mike'
from Parser import Parser
from Node import Node

def main():
    parser = Parser()
    args = parser.get_parsed_args()
    node = Node(id=args.id)
    if args.boot:
        node.start_network()

if __name__=='__main__':
    main()