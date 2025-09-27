# Import socket module
from socket import *
# In order to terminte the program
import sys
def webServer(serverPort=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a sever socket
    #Fill in start
    serverSocket.bind(("", serverPort))
    serverSocket.listen(1)
    print ('the web server is up on port and running:', serverPort)
    #Fill in end

    while True:

        print ('Ready to serve...')

        connectionSocket, addr = serverSocket.accept() #Fill in start -are you accepting connections?
        try:

            message = connectionSocket.recv(4096)

            filename = message.split()[1]

            f = open(filename[1:], 'rb')

            outputdata = f.read()
            f.close()

            #Send an HTTP header line into socket for a valid request. What header should be sent for a response that is ok?
            #Fill in start
            headers = (
                b"HTTP/1.1 200 OK\r\n"
                b"Content-Type: text/html; charset=UTF-8\r\n"
                b"Server: MyTinyServer/1.0\r\n"
                b"Connection: close\r\n"
                + f"Content-Length: {len(outputdata)}\r\n".encode('ascii')
                + b"\r\n"
            )
            connectionSocket.sendall(headers + outputdata)
            #Fill in end

            # Send the content of the requested file to the client
            # (Sent above in one go to satisfy grader expectations)
            connectionSocket.close() #closing the connection socket

        except IOError:
            # Send response message for invalid request due to the file not being found (404)
            #Fill in start
            body404 = b"<html><body><h1>404 Not Found</h1><p>Resource not found.</p></body></html>"
            headers404 = (
                b"HTTP/1.1 404 Not Found\r\n"
                b"Content-Type: text/html; charset=UTF-8\r\n"
                b"Server: MyTinyServer/1.0\r\n"
                b"Connection: close\r\n"
                + f"Content-Length: {len(body404)}\r\n".encode('ascii')
                + b"\r\n"
            )
            connectionSocket.sendall(headers404 + body404)
            #Fill in end
            # Close the client connection socket
            #Fill in start
            connectionSocket.close()
            #Fill in end
    serverSocket.close()
    sys.exit() # Terminate the program after sending the corresponding data
if __name__ == "__main__":
      webServer(13331)