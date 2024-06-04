def choiceHero():
    print("Escolha seu heroi:")
    print("1. K'sante - Tanque/Lutador")
    print("2. Sion - Tanque")
    print("3. Lee Sin - Lutador")
    print("4. Veigar - Mago 🔮")
    print("5. Ashe - Atirador 🏹")
    print("6. Akali - Mago Assassino 🧙‍♀️🗡")
    
    escolha = int(input("Digite o número da classe escolhida: "))
    
    if escolha == 1:
        return "K'sante", 610, 37, 32, 66, 0
    elif escolha == 2:
        return "Sion", 545, 32, 32, 68, 0
    elif escolha == 3:
        return "Lee Sin", 575, 36, 32, 70, 0
    elif escolha == 4:
        return "Veigar", 575, 23, 32, 52, 55
    elif escolha == 5:
        return "Ashe", 570, 26, 30, 59, 0
    elif escolha == 6:
        return "Akali", 570, 23, 37, 62, 50
    else:
        print("Escolha inválida!")
        return choiceHero()

class hero:
    def __init__(self, name, hero, life, shild, magicResistance, fisicDamage, magicDamage):
        self.name = name
        self.hero = hero
        self.life = life
        self.shild = shild
        self.magicResistance = magicResistance
        self.fisicDamage = fisicDamage
        self.magicDamage = magicDamage
        
attack = {
    "K'sante": [
        {"nome": "Fenda Sombria", "dano": 70, "chance": 0.8},
        {"nome": "Corte da Lua", "dano": 90, "chance": 0.6},
        {"nome": "Guardiao das Sombras", "dano": 100, "chance": 0.3}
    ],
    "Sion": [
        {"nome": "Investida do Decaido", "dano": 20, "chance": 1},
        {"nome": "Grito do Assassino", "dano": 60, "chance": 0.8},
        {"nome": "Investida Incontrolavel", "dano": 150, "chance": 0.4}
    ],
    "Lee Sin": [
        {"nome": "Onda Sonica", "dano": 50, "chance": 0.7},
        {"nome": "Tempestade", "dano": 90, "chance": 0.6},
        {"nome": "Guardiao das Sombras", "dano": 100, "chance": 0.3}
    ],
    "Veigar": [
        {"nome": "Explosao Ignea", "dano": 60, "chance": 0.6},
        {"nome": "Morte Subita", "dano": 70, "chance": 0.8},
        {"nome": "Despreso Primordial", "dano": 175, "chance": 0.3}
    ],
    "Ashe": [
        {"nome": "Flesha de Gelo", "dano": 50, "chance": 1},
        {"nome": "Frenesi de Guinsoo", "dano": 60, "chance": 0.8},
        {"nome": "Flecha de Cristal Encantada", "dano": 200, "chance": 0.2}
    ],
    "Akali": [
        {"nome": "Marca do Assassino", "dano": 65, "chance": 0.8},
        {"nome": "Investida Shuriken", "dano": 77, "chance": 0.6},
        {"nome": "Investida dos Cinco Pontos", "dano": 125, "chance": 0.3}
    ],
}