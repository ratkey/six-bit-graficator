# coding: utf-8
__author__ = 'CotherArt'

import pygame
import pygame_textinput
from vector import Vector
from numeros import numeros

pygame.init()
pygame.font.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGTH_BLUE =(186, 212, 239)

color_fondo = WHITE
color_linea = BLUE
color_punto = BLACK
color_texto = BLACK
color_graph = RED
color_grid = LIGTH_BLUE


# Variables
done = False
vectors = []
vector_thicknes = 2
WIDTH, HEIGHT = 1200, 300
ORIGEN = (int(WIDTH/2), int(HEIGHT/2))
text_font_size = 30
zoom = 100

myfont = pygame.font.SysFont('Consolas', 15)


# Crea el TextInput-object
textinput = pygame_textinput.TextInput(font_size=text_font_size)
textinput.set_text_color(color_texto)
textinput.set_cursor_color(color_texto)
text_margen_x = 10
text_margen_y = 25

# Dibuja el texto
def draw_num_text():
    global numeros
    for n in numeros:
        posx = ajustar_punto_en_x(n) + 2
        texto = str(n[1])
        textsurface = myfont.render(texto, True, BLACK, None)
        screen.blit(textsurface,(posx, ORIGEN[1] + 2))

# Display properties
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('six bit graficator by: CotherArt')
clock = pygame.time.Clock()

def position_conversor(punto):
    # if type(punto) is tuple:
    return (punto[0]+ORIGEN[0], -1*punto[1]+ORIGEN[1])

# Aniade un vector a la lista
def add_vector(cords):
    global vectors
    v = Vector(cords)
    vectors.append(v)

# Dibuja el vector en la pantalla
def draw_vectores():
    if len(vectors) >= 1:
        for v in vectors:
            # print(v.get_cords())
            end_pos = position_conversor(v.get_cords())
            pygame.draw.line(screen, color_linea, ORIGEN, end_pos, vector_thicknes)
            pygame.draw.circle(screen, color_punto, end_pos, 2)

# Ajustar el numero a la cuadricula
def ajustar_punto_en_x(numero):
    global zoom
    punto_en_x = numero[1] * zoom
    punto_en_x = int(punto_en_x + ORIGEN[0])
    return punto_en_x

# Dibuja los numeros el la pantalla
def draw_numeros():
    global numeros

    for n in numeros:
        punto_en_x = ajustar_punto_en_x(n)
        if n[1] == 14 or n[1] == -14:
            pygame.draw.line(screen, RED, (punto_en_x, 0), (punto_en_x, HEIGHT), 1)
        else:
            pygame.draw.line(screen, BLUE, (punto_en_x, 0), (punto_en_x, HEIGHT), 1)
        pygame.draw.circle(screen, color_punto, (punto_en_x, ORIGEN[1]), 2)


# Dibuja los ejes ene la pantalla
def draw_ejes():
    # Linea del eje X
    pygame.draw.line(screen, color_graph, (0, HEIGHT/2), (WIDTH,HEIGHT/2), 1)
    # Linea del eje Y
    pygame.draw.line(screen, color_graph, (WIDTH/2, 0), (WIDTH/2,HEIGHT), 1)


# Transforma una string en una tupla y agraga el vector
# ejemplo: '<50, 20>' => (50,20)
def add_vector_text(text):
    text = text.replace('<','')
    text = text.replace('>','')
    spl = text.split(',')
    cordenadas = (int(spl[0]), int(spl[1]))
    
    add_vector(cordenadas)

# Dibuja la cuadricula
def draw_cuadricula():
    blockSize = 20 #Set the size of the grid block
    for x in range(10, WIDTH, 10):
        pygame.draw.line(screen, color_grid, (x, 0), (x, HEIGHT), 1)
    for y in range(10, HEIGHT, 10):
        pygame.draw.line(screen, color_grid, (0, y), (WIDTH, y), 1)
    
def zoominout(num):
    global zoom 
    zoom = num

# Main loop
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    # Dibujar los elementos en la pantalla
    screen.fill(color_fondo)
    draw_cuadricula()
    draw_ejes()
    draw_vectores()
    draw_numeros()
    draw_num_text()

    # Text input events
    if textinput.update(events):
        comando = textinput.get_text()
        textinput.clear_text()

        if comando == 'clear':
            vectors.clear()
        if comando == 'zoom 1':
            zoominout(1)
        if comando == 'zoom 2':
            zoominout(10)
        if comando == 'zoom 3':
            zoominout(100) 
        if comando == 'zoom 4':
            zoominout(1000) 

    screen.blit(textinput.get_surface(), (text_margen_x, HEIGHT - text_margen_y))

    pygame.display.update()
    clock.tick(30)
    # pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))