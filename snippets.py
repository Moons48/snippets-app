import logging

#set the log output file and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)
#filename indicates where you want loggin to be saved
#The level argument sets the level

#This is creating the program skeleton and inserting stubs for each one:

def put(name, snippet):
    """
    Store a snippet with an associated name.
    Returns the name of the snippet"""
    
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
    return name, snippet
    
de get(name):
    """Retrieve the snippet with a given name.
    
    If there is no such snippet, return '404: Snippet Not Found'.
    
    Returns the snippet.
    """
    
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""
    
    