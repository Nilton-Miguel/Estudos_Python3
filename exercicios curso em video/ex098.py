from time import sleep

def contagem(inicio, fim, passo):
    index = 0
    while i <= fim:
        sleep(0.25)
        print(index, end=' ')
        index+=1
    print()

if __name__ == '__main__':
    contagem(0, 10, 1)
