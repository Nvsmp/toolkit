import requests

extensoes = [
    ".php", ".phtml", ".php3", ".php4", ".php5", ".phps", ".phar",
    ".html", ".htm", ".shtml",
    ".asp", ".aspx",
    ".jsp", ".jspx", ".jsf",
    ".cgi", ".pl",
    ".py", ".pyc", ".pyo",
    ".rb", ".erb", ".rhtml",
    ".js", ".mjs",
    ".xml", ".json", ".yaml", ".yml", ".ini", ".conf", ".config",
    ".md", ".markdown",
    ".txt", ".log", ".bak", ".old", ".zip", ".tar.gz", ".sql",
    ".db", ".sqlite", ".inc", ".swp", ".temp", ".tmp", ".backup"
]

VALID_CODES = [200, 401, 403, 301, 302, 500]
HEADERS = {"User-Agent": "Mozilla/5.0"}

def testSubDomain(host_dns):
    dominios = []
    try:
        with open("diretoriosP.txt", "r", encoding="utf-8") as file:
            palavras = file.read().splitlines()

        for palavra in palavras:
            try:
                url = f"http://{host_dns}/{palavra}"
                resp = requests.get(url, headers=HEADERS, timeout=5).status_code
                if resp in VALID_CODES:
                    print(f"[+] {url} => {resp}")
                    dominios.append(palavra)
            except:
                pass

            for ext in extensoes:
                try:
                    url = f"http://{host_dns}/{palavra}{ext}"
                    resp = requests.get(url, headers=HEADERS, timeout=5).status_code
                    if resp in VALID_CODES:
                        print(f"[+] {url} => {resp}")
                        dominios.append(f"{palavra}{ext}")
                except:
                    pass

        return dominios
    except Exception as e: 
        print(f"Erro: {e}")
        return dominios

if __name__ == "__main__":
    diretorios = testSubDomain("localhost")
    print("Encontrados:", diretorios)
