import requests

def testSubDomain(host_dns):
    dominios = []
    try:
        #print("FLAG 1")
        with open("diretoriosP.txt", "r", encoding="utf-8") as file:
            texto = file.read()
            palavras = texto.splitlines()
        #print("FLAG 2")
        for palavra in palavras:
            resp = requests.get(f"http://{host_dns}/{palavra}").status_code
            if resp != 404:
                dominios.append(palavra)
                
        #print(f"FLAG 3 : {dominios}")
        return dominios
    
    except Exception as e: 
        print(f"ERRO NO TESTE DE SUBDOMINIO : | {e}")
        return dominios

if __name__ == "__main__":
    diretorios = testSubDomain(host_dns="scanme.nmap.org")
    print(diretorios)