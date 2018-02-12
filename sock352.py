# This is the skeleton code of a cs 352 socket
# You must change the code in the pass statements to make the client and server work.

import socket as ip


class socket:
    def __init__(self):
        self.mysocket = ip.socket(ip.AF_INET, ip.SOCK_DGRAM)

    def socket(self):
        self.mysocket = ip.socket(ip.AF_INET, ip.SOCK_DGRAM)
        print ("Socket initialized")

    def bind(self, address):
        self.mysocket.bind(address)
        print ("Socket binding complete")

    def sendto(self, buffer, address):
         return self.mysocket.sendto(buffer,address)

    def recvfrom(self, nbytes):
         return self.mysocket.recvfrom(nbytes)


    def close(self):
        self.mysocket.close()# close socket connection