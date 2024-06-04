#Import area - start
import random
from src.utils.heros import choiceHero, hero
from src.utils.combat import combat
#import area - end
def championSelectPlayer1():
    print(f"O campeao escolhido pelo {player1} foi {selectHero[0]}")


player1 = input("Como se chama campeao: ")
selectHero = choiceHero()
championSelectPlayer1()