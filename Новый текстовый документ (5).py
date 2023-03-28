import pygame
from random import randint
pygame.init()

# Определяем цвета
WHITE = (0, 0, 0)
col = ['red','blue','green','orange','purple']
q = 0
# Определяем размеры окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Создаем окно
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Создаем квадрат
square_size = 25
square_x = WINDOW_WIDTH // 2 - square_size // 2
square_y = WINDOW_HEIGHT // 2 - square_size // 2
square_speed = 1
square_rect = pygame.Rect(square_x, square_y, square_size, square_size)

# Основной цикл программы
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        square_rect.move_ip(0, -square_speed)
        q = col[randint(0,4)]
    if keys[pygame.K_s]:
        square_rect.move_ip(0, square_speed)
        q = col[randint(0,4)]
    if keys[pygame.K_a]:
        square_rect.move_ip(-square_speed, 0)
        q = col[randint(0,4)]
    if keys[pygame.K_d]:
        square_rect.move_ip(square_speed, 0)
        q = col[randint(0,4)]
    
    # Обработка столкновений со стенами
    if square_rect.left < 0:
        square_rect.left = 0
    elif square_rect.right > WINDOW_WIDTH:
        square_rect.right = WINDOW_WIDTH
    if square_rect.top < 0:
        square_rect.top = 0
    elif square_rect.bottom > WINDOW_HEIGHT:
        square_rect.bottom = WINDOW_HEIGHT
    
    # Отрисовка объектов
    
    pygame.draw.rect(screen, q, square_rect)
    
    # Обновление экрана
    pygame.display.update()

# Завершение работы Pygame
pygame.quit()