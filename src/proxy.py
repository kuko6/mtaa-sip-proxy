import re
import PySipFullProxy.sipfullproxy as proxy
import socket
import socketserver
import logging
import time
import sys
from ipaddress import ip_address


# def is_number(str):
#     while True:
#         try:
#             str = int(str)
#             break
#         except ValueError:
#             return False

#     return True

def handle_input():
    while True:
        try:
            ipaddress = input("enter the host ip address:\n> ")
            tmp = ip_address(ipaddress)
            break
        except ValueError:
            print("|sorry, you've entered an invalid ip address|")

    # while True:
    #     port = input("enter the host port or leave blank for default (5060):\n> ")
    #     if (port == '' or is_number):
    #         break
    #     print("|sorry, you've entered an invalid port number|")

    return ipaddress

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='proxy.log',filemode='w',level=logging.INFO,datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    #logging.info(hostname)
    #ipaddress = socket.gethostbyname(hostname) # tuto je problem
    #print(hostname)
    #print(ipaddress)

    try: 
        ipaddress = sys.argv[1]
    except IndexError:
        ipaddress = handle_input()

    print(f"sip proxy running on {ipaddress}:{proxy.PORT}")
    logging.info(f'{hostname} - {ipaddress}:{proxy.PORT}')

    #proxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, proxy.PORT)
    #proxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, proxy.PORT)
    proxy.recordroute = f'Record-Route: <sip:{ipaddress}:{proxy.PORT};lr>'
    proxy.topvia = f'Via: SIP/2.0/UDP {ipaddress}:{proxy.PORT}'
    server = socketserver.UDPServer((proxy.HOST, proxy.PORT), proxy.UDPHandler)
    
    while True:
        try:
            server.handle_request()
        except KeyboardInterrupt:
            print("\ngoodbye :)")
            break
        
    