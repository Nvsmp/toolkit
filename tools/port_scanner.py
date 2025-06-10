import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

portas_tcp = [
     21,   22,   23,   25,   53,   80,   110,  111,  135,  139,
    143,  443,  445,  993,  995, 1025, 1026, 1027, 1028, 1029,
   1433, 1434, 1720, 1723, 1755, 1900, 2000, 2001, 2002, 3306,
   3389, 3986, 4899, 5000, 5060, 5101, 5222, 5432, 5500, 5631,
   5666, 5800, 5900, 6000, 6001, 6002, 6129, 6379, 6666, 6667,
   7000, 7070, 8000, 8008, 8080, 8081, 8443, 8888, 9000, 9090,
   9100, 9200, 9999,10000,11211,12000,12345,13782,16080,18080,
  27017,28017,49152,49153,49154,49155,49156,49157,50000,50001,
  50002,50003,50004,50005,55555,55600,32768,32769,32770,32771,
  32772,32773,32774,49158,49159,49160,49161,49163,49165,49167,
  8118, 31337, 9929
]
portas_udp = [
     53,   67,   68,   69,  123,  135,  137,  138,  161,  162,
    500,  514,  520,  631, 1434, 1645, 1646, 1812, 1813, 1900,
   2049, 2100, 2222, 2600, 2998, 3283, 3478, 3702, 4500, 4672,
   4789, 5060, 5061, 5351, 5353, 5432, 5555, 5632, 5678, 6000,
   6464, 6665, 6666, 6667, 7000, 7070, 7777, 8000, 8080, 8181,
   8888, 9000, 9100, 9876, 9987,10000,11211,12000,12345,13720,
  16080,18080,22222,27000,27005,27015,27031,27036,27037,27039,
  27099,27100,30718,31337,32768,32769,32770,32771,32772,32773,
  32774,32815,33333,34567,36866,37475,37777,40000,44444,49152,
  49153,49154,49155,49156,49157,49158,49159,50000,65535, 9, 
  8118, 31337, 9929
]

def banner_grabbing(host, ports):
    resultado = []
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(2)
            s.connect((host, port))
            s.sendall(b"HEAD / HTTP/1.1\rHost: " + host.encode() + b"\r\n\r\n")
            banner = s.recv(1024).decode(errors="ignore")
            s.close()
            #print(f"[{port}] Banner: \n{banner}]")
            #print(resultado)
            if banner == "":
                resultado.append(f"[ {port} ] \n[ EMPTY BANNER / NULL RESPONSE ]")
            else:
                resultado.append(f"[ {port} ] \n[ {banner} ]")
        except Exception as e:
            resultado.append(f"[ {port} ] \n[ ERROR : {e} ]")
    return resultado

def testar_tcp(port, host, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((host, port))
            #print(f"[TCP] PORTA {port} ABERTA\n")
            return port
    except:
        return None
    
def testar_udp(host, port, timeout=2):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(timeout)
            s.sendto(b'\x00', (host, port))
            s.recvfrom(1024)
            #print(f"[UDP] Porta {port} POSSIVELMENTE ABERTA")
            return ("UDP", port)
    except:
        return None

def scan_port(host, timeout=0.5):
    open_ports = []
    all_ports = []
    for i in range(1,65536):
        all_ports.append(i)
    with ThreadPoolExecutor(max_workers=200) as executor:
        # ALL PORTS
        tarefas_tcp = [executor.submit(testar_tcp, port, host, timeout) for port in all_ports]
        tarefas_udp = [executor.submit(testar_udp, port, host, timeout) for port in all_ports ]

        # # TOP ALGUMAS
        # tarefas_udp = [executor.submit(testar_udp, port, host, timeout) for port in portas_udp]
        # tarefas_tcp = [executor.submit(testar_tcp, port, host, timeout) for port in portas_tcp]

        for future in as_completed(tarefas_tcp + tarefas_udp):
            resultado = future.result()
            
            if resultado:
                #print(resultado)
                #print(open_ports)
                open_ports.append(resultado)

    return open_ports

if __name__ == "__main__":
    resp = socket.getservbyport(22)

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            pass
    except Exception as e:
        print(e)