#Import area - start
import random
from src.utils.heros import choiceHero, hero
from src.utils.combat import combat
#import area - end
def championSelectPlayer():
    player1 = input("Como se chama campeao: ")
    selectHero = choiceHero()
    print(f"O campeao escolhido pelo {player1} foi {selectHero[0]}\n")
    print("==============================")
    player2 = input("Como se chama campeao: ")
    selectHero = choiceHero()
    print(f"O campeao escolhido pelo {player2} foi {selectHero[0]}\n")
    
championSelectPlayer()