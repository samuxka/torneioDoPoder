# Import area - start
import random
from src.utils.heros import choiceHero, hero
from src.utils.combat import combat
# Import area - end

def welcomeToGame():
    print("BEM-VINDO AO TORNEIO DO PODER!!! 🤼‍♂️🥊🏆")
    print("Está preparado para o que está te esperando????")
    preparado = input("Está preparado? \ny/n: ")
    if preparado == "y":
        print("Perfeito! Vamos começar a jogar! Chame um amigo para batalhar com você.\n")
    elif preparado == "n":
        print("Não está preparado ainda???? Então prepare-se para a batalha!!!!\n")
        return welcomeToGame()
    else:
        print("Opção inválida!!\n")
        return welcomeToGame()

def championSelectPlayer(player_num):
    nome = input(f"Como se chama o campeão {player_num}: ")
    selectHero = choiceHero()
    print(f"Ótima escolha {nome}, o campeão escolhido foi {selectHero[0]}\n")
    return {"nome": nome, "heroi": selectHero[0]}

def evenOrOdd(jogador1, jogador2):
    print("Escolha, Par ou Ímpar?")
    print("1. Ímpar")
    print("2. Par")
    escolha = int(input("Digite sua escolha: "))
    if escolha == 1:
        escolhaJogador1 = "ímpar"
    elif escolha == 2:
        escolhaJogador1 = "par"
    else:
        print("Opção inválida!!!")
        return evenOrOdd(jogador1, jogador2)

    diceResult = random.randint(1, 6)

    print(f"O jogador {jogador1['nome']} escolheu {escolhaJogador1}")
    print(f"Resultado do dado: {diceResult}")

    if (diceResult % 2 == 0 and escolhaJogador1 == "par") or (diceResult % 2 != 0 and escolhaJogador1 == "ímpar"):
        print(f"{jogador1['nome']} começa atacando")
        return jogador1, jogador2
    else:
        print(f"{jogador2['nome']} começa atacando")
        return jogador2, jogador1

if __name__ == "__main__":
    welcomeToGame()
    jogador1 = championSelectPlayer(1)
    jogador2 = championSelectPlayer(2)
    jogadorAtacante, jogadorDefensor = evenOrOdd(jogador1, jogador2)
    # A partir daqui, você pode continuar com a lógica de combate entre `jogador_atacante` e `jogador_defensor`
