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
        print("Prefeito vamos começar a jogar! Chame um amigo para batalhar com voce")
    elif preparado == "n":
        print("Nao esta preparado ainda???? Entao prepare-se para a batalha!!!!\n")
        return welcomeToGame()
    else:
        print("Opcao invalida!!\n")
        return welcomeToGame()

def championSelectPlayer():
    player1 = input("Como se chama campeao: ")
    selectHero = choiceHero()
    print(f"O campeao escolhido por {player1} foi {selectHero[0]}\n")
    print("==============================")
    player2 = input("Como se chama campeao2: ")
    selectHero = choiceHero()
    print(f"O campeao escolhido por {player2} foi {selectHero[0]}\n")

def evenOrOdd():
    print(f"Escolha, Par ou impar?")
    print("1. Impar")
    print("2. Par")
    escolha = int(input("Digite sua escolha: "))
    if escolha == 1:
        return "Impar"
    elif escolha == 2:
        return "Par"
    else:
        print("Opcao invalida!!!")
        return evenOrOdd()

welcomeToGame()
championSelectPlayer()
evenOrOdd()
print(f"O numero escolhido foi {evenOrOdd}")