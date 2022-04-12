from time import sleep


PAREDE = '#'
CAMINHO_LIVRE = ' '
CAMINHO_PERCORRIDO = "."
ROBO = "X"
SAIDA = "S"

ESQUERDA = [0, -1]
DIREITA  = [0, 1]
CIMA     = [-1, 0]
BAIXO    = [1, 0]

LABIRINTO = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ' , ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#'], 
    ['#', '#', '#', '#', ' ', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'], 
    ['#', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#'], 
    ['#', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', ' ', '#', ' ', ' ', '#', '#', ' ', '#'], 
    ['#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
    ['#', '#', '#', '#', '#', '#', '#', '#', 'X', '#', '#', '#', '#', '#', '#', '#', '#', '#','S' , '#'],
]

def print_labirinto():
    print("")
    for linha in LABIRINTO:
        print("".join(linha))
    print("")

def movimento(posicao: tuple, direcao: list):
    LABIRINTO[posicao[0]][posicao[1]] = CAMINHO_PERCORRIDO
    LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] = ROBO
    return [posicao[0] + direcao[0], posicao[1] + direcao[1]]

def verifica_movimento(posicao: tuple, direcao: list) -> bool:
    if LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == SAIDA:
        LABIRINTO[posicao[0]][posicao[1]] = CAMINHO_PERCORRIDO
        LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] = ROBO
        print_labirinto()
        print("SUCESSO!")

    return (LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == CAMINHO_LIVRE)

def main():
    POSICAO_INICIAL = [9, 8]

    LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = ROBO

    print_labirinto()

    POSICAO_ATUAL = POSICAO_INICIAL

    for _ in range(34):
        if _ in [0,5,6,7,8,13,14,15] and verifica_movimento(POSICAO_ATUAL, CIMA):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, CIMA)
            print_labirinto()
            sleep(1)

        elif _ in [ 1,2,3,4] and verifica_movimento(POSICAO_ATUAL, ESQUERDA):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, ESQUERDA)
            print_labirinto()
            sleep(1)

        elif _ in [ 9,10,11,12,16,17,18,19,20,21,22,23,26,27] and verifica_movimento(POSICAO_ATUAL, DIREITA):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
            print_labirinto()
            sleep(1)

        elif _ in [24,25,28,29,30,31,32,33,34] and verifica_movimento(POSICAO_ATUAL, BAIXO):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, BAIXO)
            print_labirinto()
            sleep(1)

if __name__ == "__main__":
    main()
