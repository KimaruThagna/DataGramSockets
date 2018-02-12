

import socket as dsock


class socket:
    def __init__(self):
        self.mysocket = dsock.socket(dsock.AF_INET, dsock.SOCK_DGRAM)

    def socket(self):
        self.mysocket = dsock.socket(dsock.AF_INET, dsock.SOCK_DGRAM)
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
