__author__ = 'mike'
from Parser import Parser
from Node import Node

def main():
    parser = Parser()
    args = parser.parse_args()
    node = Node(args.id)

if __name__=='__main__':
    main()