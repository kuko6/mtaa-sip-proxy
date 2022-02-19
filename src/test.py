import PySipFullProxy.sipfullproxy as proxy
import socket
import socketserver
import logging
import time
import sys

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='proxy.log',filemode='w',level=logging.INFO,datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    logging.info(hostname)
    ipaddress = socket.gethostbyname(hostname)
    #print(hostname)
    #print(ipaddress)
    if ipaddress == "127.0.0.1":
        try: 
            ipaddress = sys.argv[1]
        except:
            ipaddress = input("host ip address: ")

    logging.info(ipaddress)

    proxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, proxy.PORT)
    proxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, proxy.PORT)
    server = socketserver.UDPServer((proxy.HOST, proxy.PORT), proxy.UDPHandler)
    print(f"sip proxy running on {ipaddress}:{proxy.PORT}")

    server.serve_forever()
