import pygame
import random

# Initialisiere Pygame
pygame.init()

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# Bildschirmgröße
SCREEN_WIDTH = 600  # Breiter als das Spielfeld, damit wir Platz für die UI haben
SCREEN_HEIGHT = 600

# Blockgröße
BLOCK_SIZE = 30

# Spielfeldgröße
FIELD_WIDTH = 10
FIELD_HEIGHT = 20

# Geschwindigkeit des Spiels
FPS = 120

# Formen und ihre Rotationen
SHAPES = [
    [['.....',
      '..O..',
      '..O..',
      '..O..',
      '..O..'],
     ['.....',
      '.....',
      '.....',
      'OOOO.',
      '.....']],
    [['..OO.',
      '..O..',
      '..O..',
      '.....',
      '.....'],
     ['.OOO.',
      '...O.',
      '.....',
      '.....',
      '.....'],
     ['...O.',
      '...O.',
      '..OO.',
      '.....',
      '.....'],
     ['.O...',
      '.OOO.',
      '.....',
      '.....',
      '.....']],
    [['...O.',
      '.OOO.',
      '.....',
      '.....',
      '.....'],
     ['.O...',
      '.O...',
      '.OO..',
      '.....',
      '.....'],
     ['.OOO.',
      '.O...',
      '.....',
      '.....',
      '.....'],
     ['..OO.',
      '...O.',
      '...O.',
      '.....',
      '.....']],
    [['.....',
      '.....',
      '.....',
      '.OO..',
      '.OO..']],
    [['..OO.',
      '.OO..',
      '.....',
      '.....',
      '.....'],
     ['.O...',
      '.OO..',
      '..O..',
      '.....',
      '.....']],
    [['.OO..',
      '..OO.',
      '.....',
      '.....',
      '.....'],
     ['...O.',
      '..OO.',
      '..O..',
      '.....',
      '.....']],
    [['.OOO.',
      '..O..',
      '.....',
      '.....',
      '.....'],
     ['..O..',
      '.OO..',
      '..O..',
      '.....',
      '.....'],
     ['..O..',
      '.OOO.',
      '.....',
      '.....',
      '.....'],
     ['..O..',
      '..OO.',
      '..O..',
      '.....',
      '.....']]
]

# Farben der Formen
SHAPE_COLORS = [
    (0, 255, 255),
    (0, 0, 255),
    (255, 165, 0),
    (255, 255, 0),
    (0, 255, 0),
    (255, 0, 0),
    (128, 0, 128)]

class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = SHAPE_COLORS[SHAPES.index(shape)]
        self.rotation = 0

def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(FIELD_WIDTH)] for _ in range(FIELD_HEIGHT)]

    for y in range(FIELD_HEIGHT):
        for x in range(FIELD_WIDTH):
            if (x, y) in locked_positions:
                color = locked_positions[(x, y)]
                grid[y][x] = color

    return grid

def convert_shape_format(piece):
    positions = []
    format = piece.shape[piece.rotation % len(piece.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == 'O':
                positions.append((piece.x + j, piece.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions

def valid_space(piece, grid):
    accepted_positions = [[(x, y) for x in range(FIELD_WIDTH) if grid[y][x] == BLACK] for y in range(FIELD_HEIGHT)]
    accepted_positions = [x for item in accepted_positions for x in item]

    formatted = convert_shape_format(piece)

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
    return True

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

def get_shape():
    return Piece(5, 0, random.choice(SHAPES))

def draw_text_middle(text, size, color, surface):
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    label = font.render(text, 1, color)

    surface.blit(label, (SCREEN_WIDTH / 2 - label.get_width() / 2, SCREEN_HEIGHT / 2 - label.get_height() / 2))

def draw_grid(surface, grid):
    for y in range(FIELD_HEIGHT):
        for x in range(FIELD_WIDTH):
            pygame.draw.rect(surface, grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

    draw_grid_lines(surface)

def draw_grid_lines(surface):
    for y in range(FIELD_HEIGHT):
        pygame.draw.line(surface, WHITE, (0, y * BLOCK_SIZE), (FIELD_WIDTH * BLOCK_SIZE, y * BLOCK_SIZE))
    for x in range(FIELD_WIDTH):
        pygame.draw.line(surface, WHITE, (x * BLOCK_SIZE, 0), (x * BLOCK_SIZE, FIELD_HEIGHT * BLOCK_SIZE))

def clear_rows(grid, locked):
    increment = 0
    for y in range(len(grid)-1, -1, -1):
        row = grid[y]
        if BLACK not in row:
            increment += 1
            ind = y
            for x in range(len(row)):
                try:
                    del locked[(x, y)]
                except:
                    continue

    if increment > 0:
        for key in sorted(list(locked), key=lambda k: k[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + increment)
                locked[newKey] = locked.pop(key)

    return increment

def draw_next_shape(shape, surface):
    font = pygame.font.Font(pygame.font.get_default_font(), 30)
    label = font.render('Next Shape', 1, WHITE)

    sx = FIELD_WIDTH * BLOCK_SIZE + 50
    sy = SCREEN_HEIGHT / 2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == 'O':
                pygame.draw.rect(surface, shape.color, (sx + j * BLOCK_SIZE, sy + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

    surface.blit(label, (sx + 10, sy - 30))

def draw_score(surface, score):
    font = pygame.font.Font(pygame.font.get_default_font(), 30)
    label = font.render(f'Score: {score}', 1, WHITE)

    sx = FIELD_WIDTH * BLOCK_SIZE + 50
    sy = SCREEN_HEIGHT / 2 - 200
    surface.blit(label, (sx + 10, sy))

def main():
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    points = 0  # Punktesystem einführen

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris')

    while run:
        grid = create_grid(locked_positions)
        fall_speed = 0.27

        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                elif event.key == pygame.K_UP:
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

            cleared_rows = clear_rows(grid, locked_positions)
            if cleared_rows:
                points += cleared_rows * 100  # 100 Punkte pro gelöschter Reihe

        screen.fill(BLACK)  # Hintergrund schwarz füllen
        pygame.draw.rect(screen, GRAY, (0, 0, FIELD_WIDTH * BLOCK_SIZE, FIELD_HEIGHT * BLOCK_SIZE), 5)  # Rahmen um Spielfeld

        draw_grid(screen, grid)
        draw_next_shape(next_piece, screen)
        draw_score(screen, points)  # Punkte auf dem Bildschirm anzeigen
        pygame.display.update()

        if check_lost(locked_positions):
            draw_text_middle("YOU LOST", 80, WHITE, screen)
            pygame.display.update()
            pygame.time.delay(1500)
            run = False

def main_menu():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris')

    run = True
    while run:
        screen.fill(GRAY)
        draw_text_middle('Press Any Key to Play', 60, WHITE, screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()

    pygame.quit()

main_menu()
