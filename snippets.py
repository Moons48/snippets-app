import logging
import argparse

"""Lets see if this pops up on git"""

#set the log output file and the log level
logging.basicConfig(filename='snippets.log', level=logging.DEBUG)
#filename indicates where you want loggin to be saved
#The level argument sets the level... There are a few different levels.

#This is creating the program skeleton and inserting stubs for each one:


def main():
    """Main function
        WHY DO I NEED THIS???"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description = "Store and retrieve snippets of text")
    
    subparsers = parser.add_subparsers(dest = "command", help = "Available commands")
    
    #subparser for the put command
    
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help = "Store a snippet")
    put_parser.add_argument("name", help="Name of the snippet")
    put_parser.add_argument("snippet", help = "Snippet text")
  #  get_parser = subparsers.add_parser("get", help = "Retrieve a snippet")
 #  get_parser.add_argument("name", help = "what the hell is this doing?")
    
    arguments = parser.parse_args()
    arguments = vars(arguments)
    command = arguments.pop("command")
    
    if command == "put":
        name, snippet = put(**arguments)
        print("Stored {!r} as {!r}".format(snippet, name))
    elif command == "get":
        snippet = get(**arguments)
        print("Retrieved snippet: {!r}".format(snippet))
        


    
    
def put(name, snippet):
    """
    Store a snippet with an associated name.
    
    Returns the name of the snippet"""
    
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
    
    return name, snippet
    
def get(name):
    """Retrieve the snippet with a given name.
    
    If there is no such snippet, return '404: Snippet Not Found'.
    
    Returns the snippet.
    """
    
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""

if __name__ == "__main__":
    main()