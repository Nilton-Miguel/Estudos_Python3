def escreva(texto, borda):
    tamanho = len(texto)+2*borda
    print('-'*tamanho)
    print(' '*borda +f'{texto}')
    print('-'*tamanho)

if __name__ == '__main__':
    escreva('Hello World!', 2)
