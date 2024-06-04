#Import area - start
import random
from src.utils.heros import choiceHero, hero
from src.utils.combat import combat
#import area - end

def welcomeToGame():
    print("BEM-VINDO AO TORNEIO DO PODER!!! 🤼‍♂️🥊🏆")
    print("Esta preparado para o que esta te esperando????")
    preparado=input("Esta preparado? \ny/n: ")
    if preparado == "y":
        print("Prefeito vamos começar a jogar! Chame um amigo para batalhar com voce\n")
    elif preparado == "n":
        print("Nao esta preparado ainda???? Entao prepare-se para a batalha!!!!\n")
        return welcomeToGame()
    else:
        print("Opcao invalida!!\n")
        return welcomeToGame()

def championSelectPlayer1():
    player1 = input("Como se chama campeao: ")
    selectHero = choiceHero()
    print(f"Otima escolha {player1}, o campeao escolhido foi {selectHero[0]}\n")
    
def championSelectPlayer2():
    player2 = input("Como se chama campeao: ")
    selectHero = choiceHero()
    print(f"Otima escolha {player2}, o campeao escolhido foi {selectHero[0]}\n")


def evenOrOdd():
    print(f"Escolha, Par ou impar?")
    print("1. Impar")
    print("2. Par")
    escolha = int(input("Digite sua escolha: "))
    if escolha == 1:
        escolhaJogador1 = "impar"
        escolhaJogador2 = "par"
    elif escolha == 2:
        escolhaJogador1 = "par"
        escolhaJogador2 = "impar"
    else:
        print("Opcao invalida!!!")
        return evenOrOdd()

    diceResultPlayer1 = random.randint(0, 6)
    diceResultPlayer2 = random.randint(0, 6)
    
    print(f"O jogador {player1.player1}")

if __name__ == "__main__":
    welcomeToGame()
    player1 = championSelectPlayer1()
    player2 = championSelectPlayer2()
    evenOrOdd()