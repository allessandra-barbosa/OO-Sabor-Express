from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_praca.receber_avaliacao('Ale', 9)
restaurante_praca.receber_avaliacao('Maria', 10)

restaurante_mexicano.alterar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()