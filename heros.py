def choiceHero():
    print(f"Escolha seu personagem:")
    print(f"1. Saitama - Lutador 🥊")
    print(f"2. Frank - Tanque 🛡️")
    print(f"3. Luffy - Lutador 🥊")
    print(f"4. Tristana - Atiradora 🏹")
    print(f"5. Gojo - Mago 🔮")
    print(f"6. Shaco - Assassino 🗡️")
    
    escolha = int(input("Digite o numero do personagem escolhido: "))
    
    if escolha == 1:
        #Nome, Vida, Armadura, Resistencia magica, Ataque fisico, ataque magico
        return "Saitama 🥊", 635, 60, 54, 70, 0
    elif escolha == 2:
        return "Frank 🛡️", 800, 76, 68, 53, 0
    elif escolha == 3:
        return "Luffy 🥊", 530, 54, 43, 84, 0
    elif escolha == 4:
        return "Tristana 🏹", 436, 35, 32, 64, 43
    elif escolha == 5:
        return "Gojo 🔮", 420, 30, 28, 34, 70
    elif escolha == 6:
        return "Shaco 🗡️", 450, 35, 34, 67, 34
    else:
        print("Opção invalida, digite um numero de 1 a 6!!")
        return choiceHero()
    
class hero:
    def __init__(self, nome, life, shield, magicResistance, fisicDamage, magicDamage):
        self.nome = nome
        self.life = life
        self.shield = shield
        self.magicResistance = magicResistance
        self.fisicDamage = fisicDamage
        self.magicDamage = magicDamage
    
attack = {
    "Saitama 🥊":[
        {"nome": "Soco Normal", "dano": 60},
        {"nome": "Soco Quase Serio", "dano": 90},
        {"nome": "Soco Serio", "dano": 150}
    ],
    "Frank 🛡️":[
        {"nome": "Strong Right", "dano": 40},
        {"nome": "Frank Fireball", "dano": 80},
        {"nome": "Franky Radical Beam ", "dano": 120}
    ],
    "Luffy 🥊":[
        {"nome": "Gatling", "dano": 54},
        {"nome": "Red Hawk", "dano": 77},
        {"nome": "King Kong Gun", "dano": 140}
    ],
    "Tristana 🏹":[
        {"nome": "Tiro Explosivo", "dano": 37},
        {"nome": "Tiro Rapido", "dano": 68},
        {"nome": "Tiro Destruidor", "dano": 200}
    ],
    "Gojo 🔮":[
        {"nome": "Limitless", "dano": 40},
        {"nome": "Six Eyes", "dano": 90},
        {"nome": "Unlimited Void", "dano": 220}
    ],
    "Shaco 🗡️":[
        {"nome": "Jack In The Box", "dano": 36},
        {"nome": "Two-Shiv Poison", "dano": 60},
        {"nome": "Hallucinate", "dano": 110}
    ],
}
