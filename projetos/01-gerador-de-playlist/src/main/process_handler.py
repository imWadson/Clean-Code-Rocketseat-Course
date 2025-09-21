import sys

def start () -> None:
    """Inicia o processo de interação com o usuário."""
    while True:

        command = input()
        if command == '1':
            print("inserindo musica")
        elif command == '2':
            print("Criando playlist")
        elif command == '5':
            sys.exit()
        else: print("\n comando não encontrado, tente novamente \n")
