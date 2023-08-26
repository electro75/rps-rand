from element import Element
import pygame

SCISSOR = "SCISSOR"
ROCK = "ROCK"
PAPER = "PAPER"
WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blobber")
clock = pygame.time.Clock()


def draw_env(img, img_rect):
    game_display.fill(WHITE)
    game_display.blit(img, img_rect)
    pygame.display.flip()


def main():
    # display code
    # sample elements

    myimage = pygame.image.load("assets/scissor.png")
    imagerect = myimage.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_env(myimage, imagerect)
        clock.tick(60)


if __name__ == "__main__":
    main()
