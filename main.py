from element import Element
import pygame

SCISSOR = "SCISSOR"
ROCK = "ROCK"
PAPER = "PAPER"

WHITE = (255, 255, 255)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blobber")
clock = pygame.time.Clock()


def draw_env():
    game_display.fill(WHITE)


def main():
    # display code
    # sample elements

    draw_env()


if __name__ == "__main__":
    main()
