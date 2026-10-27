from socket import *
import ssl
serverPort = 12000 # define server port
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER) # set up context as TLS server
context.load_cert_chain(certfile='server.crt', keyfile='server.key') # set up certificate and key files
serverSocket = socket(AF_INET, SOCK_STREAM) # create server socket
serverSocket.bind(('', serverPort)) # bind the socket to the port
serverSocket.listen(1) # listen for 1 incoming connection
serverSocket = context.wrap_socket(serverSocket, server_side=True) # wrap the server socket with tls context
print('The TLS server is ready to receive!') # print when connection is found
connectionSocket, addr = serverSocket.accept() # accept the connection
while True:
    message = connectionSocket.recv(2048).decode() # receive message from client        
    if message.lower() == 'exit': # check for 'exit'
        print('Exiting...') # print that program is closing
        connectionSocket.close() # closes socket
        break # jumps out of loop
    else: # message is not 'exit'
        print('From client:', message) # print incoming message
        modifiedMessage = message.upper() # modify message to be uppercase
        print('To client:', modifiedMessage) # print modified message
        connectionSocket.send(modifiedMessage.encode()) # send modified message