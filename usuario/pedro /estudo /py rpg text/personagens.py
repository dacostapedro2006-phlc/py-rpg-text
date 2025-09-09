
import itens
class personagens:
    def __init__(self, classe, nome, idade, agilidade, forca, vida):
        self.classe = classe
        self.nome = nome
        self.idade = idade
        self.forca = forca
        self.agilidade = agilidade
        self.vida = vida



    def cria_personagem(i):
        if i == 1:
            mago = personagens("Mago",input("qual o seu nome? "), input("qual a sua idade? "), 5, 3, 100)
            return mago
        elif i == 2:
            guerreiro = personagens( "Guerreiro",input("qual o seu nome?"), input("qual a sua idade?"), 3, 5, 100)
            return guerreiro

        elif i == 3:
            arqueiro = personagens("Arqueiro",input("qual o seu nome?"), input("qual a sua idade?"), 4, 4, 100)
            return arqueiro  
        

    def status_horizontal(self):
        arma_nome = self.arma.nome if hasattr(self, 'arma') else "---"
        armor_nome = self.armadura.nome if hasattr(self, 'armadura') else "---"
        return f"CLASSE: {self.classe} | NOME: {self.nome} | IDADE: {self.idade} | FORÇA: {self.forca} | AGILIDADE: {self.agilidade} | VIDA: {self.vida} |\nARMA: {arma_nome}| VIDA: {self.armor} "


    def equipar_arma(self, arma):
        self.arma = arma
        print(f"{self.nome} equipou a arma: {arma.nome}")

    def armor(self, armadura):
        self.armadura = armadura
        print(f"{self.nome} equipou a armadura: {armadura.nome}")   





class inimigos:
    def __init__(self, nome, forca, agilidade, vida):
        self.nome = nome
        self.forca = forca
        self.agilidade = agilidade
        self.vida = vida
    def inventario(self):
        self.inventario = []
class animais:
    def __init__(self, nome, forca, agilidade, vida):
        self.nome = nome
        self.forca = forca
        self.agilidade = agilidade
        self.vida = vida
class aldeoes:
    def __init__(self, nome, forca, agilidade, vida):
        self.nome = nome
        self.forca = forca
        self.agilidade = agilidade
        self.vida = vida
    
        
            
