import subprocess

def ping(host,so):
    try:
        #print(so)
        if so == "posix":
            comando = ["ping","-c","2", host]
        else:
            comando = ["ping","-n","2", host]
        #output = subprocess.check_output(f"ping {comando} 2 {host}", stderr=subprocess.DEVNULL, universal_newlines=True)  # retorna string em vez de bytes )
        output = subprocess.check_output(comando, stderr=subprocess.DEVNULL, universal_newlines=True)
        
        # Verificações simples e amplas (independente do idioma)
        if "TTL=" in output or "ttl=" in output:
            return True
        else:
            return False

    except subprocess.CalledProcessError:
        return False
    
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return False