import pygame
import random
import asyncio

pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK = 20
SPEED = 10

WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLACK = (0,0,0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 30)

def random_food(snake):
    while True:
        pos = (random.randrange(0, WIDTH, BLOCK), random.randrange(0, HEIGHT, BLOCK))
        if pos not in snake:
            return pos

async def main():
    snake = [(WIDTH//2, HEIGHT//2)]
    direction = (BLOCK, 0)
    food = random_food(snake)
    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, BLOCK):
                    direction = (0, -BLOCK)
                elif event.key == pygame.K_DOWN and direction != (0, -BLOCK):
                    direction = (0, BLOCK)
                elif event.key == pygame.K_LEFT and direction != (BLOCK, 0):
                    direction = (-BLOCK, 0)
                elif event.key == pygame.K_RIGHT and direction != (-BLOCK, 0):
                    direction = (BLOCK, 0)

        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        if (head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT or