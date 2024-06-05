import os
import random
from heros import attack

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculateDamage(baseDamage, resistance, damageType):
    if damageType == "fisico":
        return baseDamage * (1 - resistance / 100 * 0.45)
    elif damageType == "magico":
        return baseDamage * (1 - resistance / 100 * 0.30)
    return baseDamage

def combat(jogadorAtacante, jogadorDefensor):
    while jogadorAtacante.life > 0 and jogadorDefensor.life > 0:
        clear_console()
        print(f"{jogadorAtacante.nome} começa atacando!")
        
        def escolherAtaque():
            print("Selecione seu ataque: ")
            ataques = attack[jogadorAtacante.nome]
            for i, ataque in enumerate(ataques, 1):
                print(f"{i} - {ataque['nome']}")
            
            chosenAttack = int(input("Como vai atacar: "))
            if 1 <= chosenAttack <= len(ataques):
                ataque = ataques[chosenAttack - 1]
                print(f"{jogadorAtacante.nome} escolheu atacar {jogadorDefensor.nome} com {ataque['nome']}\n")
                print("=============================================================================\n")
                return ataque
            else:
                print("Opção inválida!!!")
                return escolherAtaque()
        
        ataque = escolherAtaque()
        
        def escolherDefesa():
            print("Defesas disponíveis:")
            print("1. Fugir")
            print("2. Defender")
            print("3. Contra-atacar")
            chosenDefense = int(input("Como vai se defender: "))
            if 1 <= chosenDefense <= 3:
                defenseName = ["Fugir", "Defender", "Contra-atacar"][chosenDefense - 1]
                print(f"{jogadorDefensor.nome} escolheu {defenseName}\n")
                print("=============================================================================\n")
                return chosenDefense
            else:
                print("Opção inválida")
                return escolherDefesa()
        
        chosenDefense = escolherDefesa()
        
        print("Rolando dados... 🎲")
        print(f"Potencializando ataque do {jogadorAtacante.nome}...")
        diceAttack = random.randint(0, 50)
        print(f"Dano Potencializado em {diceAttack}%")
        
        print("Rolando dado... 🎲")
        print(f"Vendo se {jogadorDefensor.nome} conseguiu se defender...")
        diceDefense = random.randint(0, 100)
        print(f"Resultado do dado de defesa: {diceDefense}")
        
        damageType = "fisico" if jogadorAtacante.magicDamage == 0 else "magico"
        print(f"Tipo de dano: {damageType}")
        
        totalDamage = calculateDamage(
            ataque["dano"], 
            jogadorDefensor.shield if damageType == "fisico" else jogadorDefensor.magicResistance, 
            damageType
        ) * (1 + diceAttack / 100)
        
        if chosenDefense == 1 and diceDefense < 20:
            print(f"{jogadorDefensor.nome} conseguiu fugir!\n")
            print("=============================================================================\n")
            totalDamage = 0
        elif chosenDefense == 2 and diceDefense < 50:
            print(f"A defesa de {jogadorDefensor.nome} funcionou!\n")
            print("=============================================================================\n")
            totalDamage /= 2
        elif chosenDefense == 3 and diceDefense < 30:
            print(f"{jogadorDefensor.nome} conseguiu contra-atacar!\n")
            print("=============================================================================\n")
            totalDamage /= 3
            jogadorAtacante.life -= totalDamage
        else:
            print("A defesa falhou!")
        
        jogadorDefensor.life -= totalDamage
        print(f"{jogadorDefensor.nome} recebeu {totalDamage:.2f} de dano")
        
        print(f"Vida restante do {jogadorAtacante.nome}: {jogadorAtacante.life:.2f}")
        print(f"Vida restante do {jogadorDefensor.nome}: {jogadorDefensor.life:.2f}\n")
        print("=============================================================================\n")
        
        jogadorAtacante, jogadorDefensor = jogadorDefensor, jogadorAtacante
        
    if jogadorAtacante.life <= 0:
        print(f"{jogadorAtacante.nome} foi derrotado! {jogadorDefensor.nome} é o grande vencedor do Torneio do Poder 🥊🏆🏅")
    else:
        print(f"{jogadorDefensor.nome} foi derrotado! {jogadorAtacante.nome} é o grande vencedor do Torneio do Poder 🥊🏆🏅")
