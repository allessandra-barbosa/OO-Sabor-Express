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
print(restaurante1)