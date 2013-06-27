__author__ = 'arpit'

import sys, socket

exchangeIp = "127.0.0.1"
exchangePort = 9006


def main():
    print "Started the player interface"
    HOST, PORT = exchangeIp, exchangePort
    data = "sdx_offload:asB,{asA:asC}"
     # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(data)

        # Receive data from the server and shut down
        received = sock.recv(1024)
    finally:
        sock.close()

    print "Sent:     {}".format(data)
    print "Received: {}".format(received)



if __name__=="__main__":
    main()