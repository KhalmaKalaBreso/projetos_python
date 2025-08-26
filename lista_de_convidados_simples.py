# Lista de convidados para o casamento de um amigo
convidados = ["convidado1", "convidado2", "convidado3", "convidado4", "convidado5", "convidado6"]

def pode_entrar(nome):
    return nome.lower().strip() in [c.lower() for c in convidados]

def main():
    nome = input("Digite o nome do convidado: ")
    if pode_entrar(nome):
        print(f"Opa {nome}! Encontrei seu nome na lista, pode entrar na festa.")
    else:
        print(f"Desculpa {nome}! Mas você não está na lista de convidados.")

if __name__ == "__main__":
    main()