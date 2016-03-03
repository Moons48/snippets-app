import logging
import argparse

"""Lets see if this pops up on git"""

#set the log output file and the log level
logging.basicConfig(filename='snippets.log', level=logging.DEBUG)
#filename indicates where you want loggin to be saved
#The level argument sets the level

#This is creating the program skeleton and inserting stubs for each one:


def main():
    """Main function
        WHY DO I NEED THIS???"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description = "Store and retrieve snippets of text")
    
    subparsers = parser.add_parser("put", help = "Store a snippet")
    arguments = parser.parse_args()
    
if __name__ == "__main__":
    main()

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
