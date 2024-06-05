import random
from heros import choiceHero, hero
from combat import calculateDamage, combat

def welcomeToGame():
    print("=============================================================================\n")
    print("BEM VINDO AO TORNEIO DO PODER!!! 🤼🏆")
    print("Esta preparado para o que esta te esperando???")
    preparado=input("Esta preparado???\nY/N: ")
    if preparado == "y":
        print("PERFEITO!!! Vamos começar a jogar! Chame um amigo para batalhar com voce!!!\n")
        print("=============================================================================\n")
    elif preparado == "n":
        print("NÃO ESTA PREPARADO??? Então prepare-se para a batalha\n")
        return welcomeToGame()
    else:
        print("Opção invalida!!! Digite y ou n\n")
        return welcomeToGame()
    
def championSelectPlayer(playerNum):
    nome, life, shield, magicResistance, fisicDamage, magicDamage = choiceHero()
    print(f"Otima escolha, o campeão escolhido foi {nome}\n")
    print("=============================================================================\n")
    return hero(nome, life, shield, magicResistance, fisicDamage, magicDamage)

def evenOrOdd(jogador1, jogador2):
    print("Esolha, Par ou Impar? 🎲")
    print("1. Impar\n2. Par")
    escolha=int(input("Digite sua escolha: "))
    if escolha == 1:
        escolhaJogador1 =  "Impar"
    elif escolha == 2:
        escolhaJogador1 = "Par"
    else:
        print("Opção invalida!!!")
        return evenOrOdd(jogador1, jogador2)
    
    diceResult = random.randint(1, 6)
    
    print(f"O jogador {jogador1.nome} escolheu {escolhaJogador1}")
    print(f"Resultado do dado: {diceResult}")
    
    if (diceResult % 2 == 0 and escolhaJogador1 == "Par") or (diceResult % 2 != 0 and escolhaJogador1 == "Impar"):
        print(f"{jogador1.nome} começa atacando\n")
        print("=============================================================================\n")
        return jogador1, jogador2
    else:
        print(f"{jogador2.nome} começa atacando\n")
        print("=============================================================================\n")
        return jogador2, jogador1

if __name__ == "__main__":
    welcomeToGame()
    jogador1 = championSelectPlayer(1)
    jogador2 = championSelectPlayer(2)
    jogadorAtacante, jogadorDefensor = evenOrOdd(jogador1, jogador2)
    combat(jogadorAtacante, jogadorDefensor)
