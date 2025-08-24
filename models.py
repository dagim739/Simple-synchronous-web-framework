from connection_layer import db_connect
cnx = db_connect() # !!!!!! This object must be properly closed after use
# put cnx.close() inside the BaseManager class
print (cnx)