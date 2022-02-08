if __name__ == "__main__":
    
    class Verbete:
        def __init__(self, nome, significado):
            self.nome = nome
            self.significado = significado
    
    palavra = Verbete('queijo', 'alimento feito à base de leite envelhecido')

    print( palavra.nome )
    print( palavra.significado )
