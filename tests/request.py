import requests

link = f"http://scanme.nmap.org/shared"

resp_get = requests.get(url=link)

print( f"HEADERS : \n{resp_get.headers}\n\nCONTENT : \n{resp_get.content}\n\nTEXT : \n{resp_get.text}\n\nCOOKIES : \n{resp_get.cookies.items() }\n\n" )


print( resp_get.cookies.list_domains() )