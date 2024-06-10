from modelos.restaurante import Restaurante

class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota