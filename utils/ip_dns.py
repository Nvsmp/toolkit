import ipaddress
import socket

def eh_ip(input):
    try:
        ipaddress.ip_address(input)
        return True
    except ValueError:
        return False
    
def getHost(target): # tem que retornar tupla ( ip , dns )
    if eh_ip(target):
        resp = socket.gethostbyaddr(target)
        return resp[2][0], resp[0]
    else:
        resp = socket.gethostbyname_ex(target)
        return resp[2][0], resp[0]

if __name__ == "__main__":
    #link = "scanme.nmap.org" 
    link = "45.33.32.156"
    #print( getHost(target=link) )  
    teste, tupla = getHost(target=link)
    print(f"TESTE : {teste} \nTUPLA : {tupla}")