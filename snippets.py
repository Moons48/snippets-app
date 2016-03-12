import logging
import argparse
import psycopg2


"""Lets see if this pops up on git"""

#set the log output file and the log level
logging.basicConfig(filename='snippets.log', level=logging.DEBUG)
#filename indicates where you want loggin to be saved
#The level argument sets the level... There are a few different levels.

#This is creating the program skeleton and inserting stubs for each one:
connection = 0

def main():
    """Main function
        WHY DO I NEED THIS???"""
    logging.info("Constructing parser")
    logging.debug("Connecting to PostgreSQL")
    global connection
    connection = psycopg2.connect(database="snippets")
    logging.debug("Database connection established.")
    parser = argparse.ArgumentParser(description = "Store and retrieve snippets of text")
    
    subparsers = parser.add_subparsers(dest = "command", help = "Available commands")
    #explain this
    
    #subparser for the put command
    
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help = "Store a snippet")
    put_parser.add_argument("name", help="Name of the snippet")
    put_parser.add_argument("snippet", help = "Snippet text")
    get_parser = subparsers.add_parser("get", help = "Retrieve a snippet")
    get_parser.add_argument("name", help="Name of the snippet") #didnt have add argument
    
    arguments = parser.parse_args()
    arguments = vars(arguments)
    command = arguments.pop("command")
    
    if command == "put":
        name, snippet = put(**arguments)
    elif command == "get":
        snippet = get(**arguments)
        print("Retrieved snippet: %s"%(snippet))
        

def put(name, snippet):
    global connection #Had to make connection global to work
    logging.info("Storing snippet %s: %s"%(name, snippet))
    with connection, connection.cursor() as cursor: #allow us to run sql commands in a script
    	command = "insert into snippets values (%s, %s)" #these are sql commands
    	try:
    		cursor.execute(command, (name, snippet)) #running command to the database
    		print("Stored %s as %s")%(snippet, name)
    	except:
    		print ("The keyword %s already exists!")%(name)
    #?still not sure about why (name, snippet)???
    connection.commit()#save the changes to the database
    logging.debug("Snippet stored successfully.")
    return name, snippet
    
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
    
    return name, snippet
    
def get(name):
    global connection
    logging.info("Retrieving snippet %s" %(name))
    with connection, connection.cursor() as cursor:
		cursor.execute("select message from snippets where keyword = %s", (name,))
		row = cursor.fetchone()
    if not row:
    	#No snippet was found
    	return "404: Snippet not found"
    return row[0]
    logging.debug("Snippet retrieved successfully. I hope")


    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return name

if __name__ == "__main__":
    main()


"""So these are all positional arguments, not option arguments that actually
	do things like the fib one I did before"""