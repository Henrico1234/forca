import random
from os import system, name

def limpa_tela():
    if name =='nt':
        _ = system("cls")

    else:
        _ = system("clear")

def game():
    
    limpa_tela()


    print("Bem-Vindo(a) ao jogo da forca")
    print("adivinhe a palavra abaixo")

    lista = ["cachorro", "banana", "celular", "praia", "livro", "computador", "universo", "floresta", "montanha", "oceano", "bicicleta", "amizade", "planeta", "jardim", "fotografia", "aventura", "mistério", "tecnologia", "sonho", "musica", "chocolate", "estrela", "viagem", "história", "arte"]

    palavra = random.choice(lista)



    letras_descobertas = ["_" for letra in palavra]
    
    chances = len(palavra)
    
    letra_erradas = []
    
    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("lestras erradas:", " ".join(letras_erradas))
        
        tentativa = input("\nDigite uma letra: ").lower()
        
        
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1  
        else:
            chances -= 1
            letras_erradas.append(tentativa)
                
        if "_" not in letras_descobertas:
            print("\n Você venceu, a palavva era: ", palavra)
            break
    else:
        print("\nVocê perdeu! A palavra era:", palavra)

if __name__ == "__main__":
    game()