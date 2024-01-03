import pygame
import random

pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pedra, Papel e Tesoura")

cores = {
    'branco': (255, 255, 255),
    'vermelho': (255, 0, 0),
    'verde': (0, 255, 0),
    'azul': (0, 0, 255),
}

fonte = pygame.font.Font(None, 36)

def exibir_mensagem(mensagem, cor, y):
    texto = fonte.render(mensagem, True, cor)
    tela.blit(texto, (largura // 2 - texto.get_width() // 2, y))

def jogo():
    escolhas = ["Pedra", "Papel", "Tesoura"]
    escolha_jogador = None

    while escolha_jogador is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    escolha_jogador = "Pedra"
                elif event.key == pygame.K_2:
                    escolha_jogador = "Papel"
                elif event.key == pygame.K_3:
                    escolha_jogador = "Tesoura"

        tela.fill(cores['branco'])
        exibir_mensagem("Escolha: 1-Pedra, 2-Papel, 3-Tesoura", cores['vermelho'], 50)
        exibir_mensagem("Pressione a tecla correspondente à sua escolha.", cores['verde'], 100)

        pygame.display.update()

    escolha_computador = random.choice(escolhas)

    resultado = verificar_vencedor(escolha_jogador, escolha_computador)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return

        tela.fill(cores['branco'])
        exibir_mensagem(f"Jogador: {escolha_jogador}", cores['verde'], 50)
        exibir_mensagem(f"Computador: {escolha_computador}", cores['azul'], 100)
        exibir_mensagem(resultado, cores['vermelho'], 150)
        exibir_mensagem("Pressione Enter para jogar novamente ou ESC para sair.", cores['verde'], 200)

        pygame.display.update()

def verificar_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate!"
    elif (
        (jogador == "Pedra" and computador == "Tesoura") or
        (jogador == "Papel" and computador == "Pedra") or
        (jogador == "Tesoura" and computador == "Papel")
    ):
        return "Você venceu!"
    else:
        return "Você perdeu!"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()

    jogo()
 