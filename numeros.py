import math
import questionary

DIGITAR = "Digitar um número"
EXEMPLOS = "Ver os casos de teste"
SAIR = "Sair"

def converter(texto):
    texto = texto.strip().replace(",", ".")
    try:
        return int(texto)
    except ValueError:
        numero = float(texto)
        if not math.isfinite(numero):
            raise ValueError("número inválido")
        return numero

def classificar(numero):
    if numero > 0:
        return "POSITIVO"
    if numero < 0:
        return "NEGATIVO"
    return "NULO"

def mensagem(numero):
    return f"O número {numero} é {classificar(numero)}."

def validar(texto):
    try:
        converter(texto)
        return True
    except ValueError:
        return "Digite um número válido, como 15, -8 ou 0."

def main():
    while True:
        opcao = questionary.select(
            "O que você quer fazer? (use as setas)",
            choices=[DIGITAR, EXEMPLOS, SAIR],
        ).ask()

        if opcao == DIGITAR:
            texto = questionary.text("Número:", validate=validar).ask()
            if texto is None:
                break
            print(mensagem(converter(texto)))
        elif opcao == EXEMPLOS:
            for numero in (15, -8, 0):
                print(mensagem(numero))
        else:
            break

if __name__ == "__main__":
    main()
