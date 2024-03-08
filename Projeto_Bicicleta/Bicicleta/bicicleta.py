
class Bicicleta:
    def __init__(self, nome, modelo, velocidade):
        self.nome = nome
        self.modelo = modelo
        self.velocidade = velocidade

    def imprirmirAtributosDaBicicleta(self):
        return self.nome, self.modelo, self.velocidade

    def imprimirNomeMaiusculo(self):
        return self.nome.upper()

    def imprimirPrimeiraLetraMaisculaDoNome(self):
        return self.nome.capitalize()

    def dobrarAVelocidadeDaBicicleta(self):
       return self.velocidade * 2