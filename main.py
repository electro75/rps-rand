from element import Element
import pygame

SCISSOR = "SCISSOR"
ROCK = "ROCK"
PAPER = "PAPER"
WIDTH = 1080
HEIGHT = 600

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption("Blobber")
clock = pygame.time.Clock()


def draw_env(img, img_rect):
    screen.fill(WHITE)
    screen.blit(img, img_rect)
    img_rect = img_rect.move(1, -1)
    screen.blit(img, img_rect)
    pygame.display.update()
    return img_rect
    


def main():
    # display code
    # sample elements

    myimage = pygame.image.load("assets/scissor.png").convert_alpha()
    myimage = pygame.transform.scale(myimage, (50, 50))
    imagerect = myimage.get_rect()
    imagerect[0] = 300
    imagerect[1] = 500

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        imagerect = draw_env(myimage, imagerect)
        clock.tick(60)


if __name__ == "__main__":
    main()
