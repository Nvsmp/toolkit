# t# Toolkit: Footprinting CLI em Python

Ferramenta de footprinting e enumeração básica feita em Python

## Funcionalidades

- 🔍 Resolução de DNS
- 📶 Teste de conectividade (ping)
- 🚪 Scan de portas
- 🪪 Banner grabbing
- 🌐 Enumeração de subdiretórios

## Uso

```bash
python3 main.py -s [alvo] ## Testa ping, Resolve o DNS, scaneia portas e captura os banners
python3 main.py -d -s [alvo] ## Adicionalmente testa subdiretórios

ex : python3 main.py -d -s scanme.nmap.org
