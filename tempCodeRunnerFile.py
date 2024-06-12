from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Ale', 9)
restaurante_praca.receber_avaliacao('Maria', 10)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()