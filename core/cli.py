import argparse, sys, os, time
from colorama import Fore, Style, init
from utils.ping import *
from utils.ip_dns import *

from tools.sub_domains import testSubDomain
from tools.port_scanner import scan_port, banner_grabbing

#  __  __       _        _ _    _ _   
# |  \/  | __ _| |_ _ __(_) | _(_) |_ 
# | |\/| |/ _` | __| '__| | |/ / | __|
# | |  | | (_| | |_| |  | |   <| | |_ 
# |_|  |_|\__,_|\__|_|  |_|_|\_\_|\__|
    
def print_banner():
    init(autoreset=True)
    print(Fore.GREEN + r"""
  _____                  _               _  __     _____  
 |_   _|  ___     ___   | |             | |/ /  _ |_   _| 
   | |   / _ \   / _ \  | |      _____  | ' /  (_)  | |   
   | |  | | | | | | | | | |     |____ | |  <    _   | | 
   | |  | |_| | | |_| | | |____         | . \  | |  | |  
   |_|   \___/   \___/  |______|        |_|\_\ |_|  |_|  
                      by Bottom Text
==========================================================
          
    """ + Style.RESET_ALL)

def run_cli():

    start = time.time()
    os.system("cls" if os.name == "nt" else "clear")    
    print_banner()
    print(Fore.CYAN + f"[ {sys.platform} ]" + Style.RESET_ALL)

    parser = argparse.ArgumentParser(description="Toolkit de Footprinting e Reconhecimento")
    parser.add_argument("-s", "--scan", help="Host a ser escaneado (ex: scanme.nmap.org)", type=str)
    parser.add_argument("-d", "--dirscan", help="Ativa a enumeração de subdiretórios", action="store_true")

    args = parser.parse_args()
    
    if args.__dict__.get("scan") is not None:   # [-S]CAN [-s] [--scan] [--SCAN]
        scan_target = args.__dict__.get("scan")
        print( Fore.GREEN +  f"SCAN - {scan_target}" + Style.RESET_ALL)   
        print( Fore.GREEN +  f"RESOLVENDO {scan_target}" + Style.RESET_ALL) 
        target_ip,target_dns = getHost(scan_target) #########################
        print( Fore.GREEN + f"[ IP ] {target_ip}" + Style.RESET_ALL) 

        if ping(target_ip, os.name):
            print( Fore.GREEN +  "PING OK" + Style.RESET_ALL)
            print( Fore.GREEN +  "TESTANDO PORTAS" + Style.RESET_ALL)
            portas = scan_port(host=target_ip)
            print( Fore.GREEN+ f"PORTAS ABERTAS : {portas}\n" + Style.RESET_ALL)
            banners = banner_grabbing(ports=portas, host=target_ip) 
            #print(banners)
            if len(banners) > 0:
                for i in banners:
                    print( Fore.LIGHTMAGENTA_EX + i + Style.RESET_ALL )
            else:
                print( Fore.RED +  "BANNERS FALHARAM" + Style.RESET_ALL)    
        else:
            print( Fore.RED +  "PING FALHOU" + Style.RESET_ALL)
    else: print( Fore.RED +  "SCAN" + Style.RESET_ALL)

    if args.__dict__.get("d") is not None: # SUB [-D]IRETORIOS [-d] 
        if ping(target_ip):
            print( Fore.GREEN +  "TESTANDO SUBDIRETORIOS" + Style.RESET_ALL)
            dominios = testSubDomain(host_dns=target_dns)
            if len( dominios ) > 0:
                for d in dominios:
                    print( Fore.LIGHTGREEN_EX +  f"SUBDIRETORIOS ENCONTRADOS : {d}" + Style.RESET_ALL)
            else: 
                print( Fore.RED +  "SUBDIRETORIOS FALHARAM" + Style.RESET_ALL)
        else:
            print( Fore.RED +  "PING FALHOU" + Style.RESET_ALL)
    else: print( Fore.RED +  "SUB DIRETORIOS" + Style.RESET_ALL)

    end = time.time()
    print( Fore.BLUE + f"TEMPO GASTO : {end-start:.2f} s\n" + Style.RESET_ALL)
    print( Fore.LIGHTMAGENTA_EX + "bottom text" + Style.RESET_ALL )