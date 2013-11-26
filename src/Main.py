__author__ = 'mike'
from Parser import Parser
from Node import Node

def main():
    parser = Parser()
    args = parser.parse_args()
    parsed = {}
    node_id = args.boot
    parsed["id":node_id]
    node = Node(parsed)

if __name__=='__main__':
    main()