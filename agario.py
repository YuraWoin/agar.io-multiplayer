from math import hypot
from random import randint
import pygame
from socket import *
from threading import Thread

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(("localhost", 8080))

my_data = sock.recv(64).decode().strip().split(",")

my_data_int_list = List(map(int, my_data_int_list))

my_id = my_data_int_list[0]
my_player = my_data_int_list[1:]

sock.setblocking(False)

pygame.init()

WIDTH = 600
HEIGHT = 600
FPS = 60
running = True

WHITE = (255, 255, 255)

my_font = pygame.font.Font(None, 50)

all_players = []
lose = False

def get_enemies_data():
    global all_players, running, lose
    while 1:
        try:
            data = sock.recv(4096).decode().strip()
            if data == "LOSE":
                lose = True
            elif data:
                parts = data.strip("|").split("|")
                for p in parts:
                    if len(p.split(",")) == 4:
                        all_players.append(list(map(int, p.split(","))))
        except:
            pass

# my_player = [0, 0, 20]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Havka:

    def __init__(self, x, y, r, c):
        self.x = x
        self.y = y
        self.r = r
        self.c = c

    def check_collision(self, px, py, pr):
        dx = self.x - px
        dy = self.y - py
        return hypot(dx, dy) <= self.r + pr


many_food = [
    Havka(
        randint(-2000, 2000),
        randint(-2000, 2000),
        10,
        (randint(0, 255), randint(0, 255), randint(0, 255)),
    )
    for _ in range(300)
]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)

    scale = max(0.3, min(50 / my_player[2], 1.5))

    pygame.draw.circle(
        screen, (0, 255, 0), (300, 300), int(my_player[2] * scale)
    )

    to_remove = []

    for food in many_food:
        if food.check_collision(my_player[0], my_player[1], my_player[2]):
            to_remove.append(food)
            my_player[2] += int(food.r * 0.2)
        else:
            fx = int((food.x - my_player[0]) * scale + 300)
            fy = int((food.y - my_player[1]) * scale + 300)
            pygame.draw.circle(screen, food.c, (fx, fy), int(food.r * scale))

    for food in to_remove:
        many_food.remove(food)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        my_player[1] -= 5
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        my_player[1] += 5
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        my_player[0] -= 5
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        my_player[0] += 5

    pygame.display.flip()
    clock.tick(FPS)
