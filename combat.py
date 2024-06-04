import random
from heros import attack

def calculateDamage(baseDamage, resistance, type):
    if type == "fisico":
        return baseDamage * (1 - resistance / 100 * 0.45)
    elif type == "magico":
        return baseDamage * (1 - resistance / 100 * 0.30)
    return baseDamage

def combat(jogadorAtacante, jogadorDefensor):
    while jogadorAtacante.life > 0 and jogadorDefensor.life > 0:
        print(f"{jogadorAtacante.nome} começa atacando")
        print("Selecione seu ataque")
        ataques = attack[jogadorAtacante.nome]
        for i, ataque in enumerate(ataques, 1):
            print(f"{i}-{ataque['nome']}")

        chosenAttack = int(input("Digite sua escolha de ataque: "))
        ataque = ataques[chosenAttack - 1]

        print(f"{jogadorAtacante.nome} escolheu atacar {jogadorDefensor.nome} com {ataque['nome']}\n")
        print("Selecione sua defesa:")
        print("1-Fugir")
        print("2-Defender")
        print("3-Contra-atacar")

        chosenDefense = int(input("Digite sua escolha de defesa: "))
        defenseName = ["Fugir", "Defender", "Contra-atacar"][chosenDefense - 1]

        print(f"{jogadorDefensor.nome} escolheu {defenseName}\n")

        print(f"Rolando dado... Potencializando ataque do {jogadorAtacante.nome}...")
        diceAttack = random.randint(0, 50)
        print(f"Dano potencializado em {diceAttack}%")

        print("Rolando dado para ver se a defesa funcionou...")
        diceDefense = random.randint(0, 100)
        print(f"Resultado do dado de defesa: {diceDefense}")

        typeDamage = "fisico" if jogadorAtacante.magicDamage == 0 else "magico"
        totalDamage = calculateDamage(ataque["dano"], jogadorDefensor.shield if typeDamage == "fisico" else jogadorDefensor.magicResistance, typeDamage) * (1 + diceAttack / 100)

        if chosenDefense == 1 and diceDefense < 20:
            print(f"{jogadorDefensor.nome} conseguiu fugir!\n")
            totalDamage = 0
        elif chosenDefense == 2 and diceDefense < 50:
            print(f"A defesa de {jogadorDefensor.nome} funcionou!\n")
            totalDamage /= 2
        elif chosenDefense == 3 and diceDefense < 30:
            print(f"{jogadorDefensor.nome} contra-atacou!\n")
            totalDamage /= 3
            jogadorAtacante.life -= totalDamage
        else:
            print(f"A defesa falhou!")

        jogadorDefensor.life -= totalDamage
        print(f"{jogadorDefensor.nome} tomou {totalDamage:.2f} de dano")

        print(f"life do {jogadorAtacante.nome} restante: {jogadorAtacante.life:.2f}")
        print(f"life do {jogadorDefensor.nome} restante: {jogadorDefensor.life:.2f}\n")

        jogadorAtacante, jogadorDefensor = jogadorDefensor, jogadorAtacante

    if jogadorAtacante.life <= 0:
        print(f"{jogadorAtacante.nome} foi derrotado! {jogadorDefensor.nome} é o vencedor!")
    else:
        print(f"{jogadorDefensor.nome} foi derrotado! {jogadorAtacante.nome} é o vencedor!")
