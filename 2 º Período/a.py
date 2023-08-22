import sys

def get_user_name():
    if sys.version_info >= (3, 0):
        return input("Por favor, digite seu nome: ")
    else:
        return raw_input("Por favor, digite seu nome: ")

def greet_user(name):
    print("Olá, {}! Bem-vindo!".format(name))

def main():
    try:
        name = get_user_name()
        greet_user(name)
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
    except Exception as e:
        print("Ocorreu um erro: {}".format(e))

if __name__ == "__main__":
    main()






