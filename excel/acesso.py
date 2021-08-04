import getpass

usuario = getpass.getuser()
senha = input(getpass.getpass("Digite a senha: "))

if usuario == "computerian" and senha == "mak":
    print("Usuário logado")
else:
    print("Login Negado")