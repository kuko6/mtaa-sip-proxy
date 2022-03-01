import re
import PySipFullProxy.sipfullproxy as proxy
import socket
import socketserver
import logging
import time
import sys
from ipaddress import ip_address


def handle_input():
    while True:
        try:
            ipaddress = input("napiste ip adresu proxy:\n> ")
            tmp = ip_address(ipaddress)
            break
        except ValueError:
            print("|sorry, napisali ste zlu ip adresu|")

    return ipaddress

def main():
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='dennik_hovorov.log',filemode='a',level=logging.INFO,datefmt='%H:%M:%S')
    logging.info(time.strftime("==|%a, %d %b %Y %H:%M:%S|==", time.localtime()))
    hostname = socket.gethostname()

    try: 
        ipaddress = sys.argv[1]
    except IndexError:
        ipaddress = handle_input()

    print(f'Proxy bezi na {ipaddress}:{proxy.PORT}')
    logging.info(f'Proxy bezi na {hostname} - {ipaddress}:{proxy.PORT}')

    proxy.recordroute = f'Record-Route: <sip:{ipaddress}:{proxy.PORT};lr>'
    proxy.topvia = f'Via: SIP/2.0/UDP {ipaddress}:{proxy.PORT}'
    server = socketserver.UDPServer((proxy.HOST, proxy.PORT), proxy.UDPHandler)
    
    while True:
        try:
            server.handle_request()
        except KeyboardInterrupt:
            print("\dovidenia :)")
            break
        

if __name__ == '__main__':
    main()
    