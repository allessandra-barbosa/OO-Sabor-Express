class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
    
    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'

musica1 = Musica('Se', 'Djavan', 300)

print('Música favorita')
print(musica1)

print('------------------------------------')

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'

carro1 = Carro('Onix', 'Branco', 2013)
carro2 = Carro('HRV', 'Vinho', 2018)
carro3 = Carro('Compass', 'Preto e Branco', 2020)

print('Meus futuros carros')
print(carro1)
print(carro2)
print(carro3)

print('------------------------------------')

class Restaurante:
    def __init__(self, nome, categoria, ativo, capacidade, telefone):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.telefone = telefone

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo} | {self.capacidade} | {self.telefone}'

restaurante1 = Restaurante('Lanchinho Feliz', 'Lanche', True, 'Rua Lago, 216', 119999999)

print('Restaurantes')
print(restaurante1)