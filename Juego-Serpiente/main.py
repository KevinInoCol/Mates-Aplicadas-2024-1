#Parte 1: Configuraciones Iniciales
import pygame #Libreria 1
import random #Libreria 2

try:
    pygame.init()
    pygame.display.set_caption("Juego Serpiente")
    largo, alto = 600, 400
    pantalla = pygame.display.set_mode((largo, alto))
    reloj = pygame.time.Clock()
except Exception as e:
    print(f"Error al inicializar Pygame: {e}")

#        R,    G,    B    - 0-255
negro  = (0,   0,   0)   #Este es para el fondo de la pantalla
blanco = (255, 255, 255) #Este es para la serpiente
rojo   = (255, 0,   0)   #Para las vidas
verde  = (0,   255, 0)   #Para la comida

tamano_cuadrado     = 20
velocidad_juego = 10

def generar_comida():
    #                          (0, 580)
    comida_x = round(random.randrange(0, largo - tamano_cuadrado) / 20) * 20
    #                          (0, 380)
    comida_y = round(random.randrange(0, alto - tamano_cuadrado) / 20) * 20
    return comida_x, comida_y #Estos dos numeros van a ser aleatorios


def disenar_comida(tamano, comida_x, comida_y):
    pygame.draw.rect(pantalla, verde, [comida_x, comida_y, tamano, tamano]) #draw es dibujar

def disenar_serpiente(tamano, pixels):
    for pixel in pixels:
        pygame.draw.rect(pantalla, blanco, [pixel[0], pixel[1], tamano, tamano])

def disenar_puntuacion(puntuacion):
    fuente = pygame.font.SysFont("Helvetica", 35) #Tipo de letra
    texto = fuente.render(f"Punto: {puntuacion}", True, rojo)
    pantalla.blit(texto, [1,1])

def seleccionar_velocidad(tecla):
    if tecla == pygame.K_DOWN:
        velocidad_x = 0
        velocidad_y = tamano_cuadrado
    if tecla == pygame.K_UP:
        velocidad_x = 0
        velocidad_y = -tamano_cuadrado
    if tecla == pygame.K_RIGHT:
        velocidad_x = tamano_cuadrado
        velocidad_y = 0
    if tecla == pygame.K_LEFT:
        velocidad_x = -tamano_cuadrado
        velocidad_y = 0
    return velocidad_x, velocidad_y

def correr_juego():
    fin_juego = False #0

    x = largo/2 #300
    y = alto/2 #200

    velocidad_x = 0
    velocidad_y = 0

    tamano_serpiente = 1
    pixels = []

    comida_x, comida_y = generar_comida()

    while not fin_juego:
        pantalla.fill(negro) #Fill es llenar / lleno de negro
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fin_juego = True #1
            elif evento.type == pygame.KEYDOWN:
                velocidad_x, velocidad_y = seleccionar_velocidad(evento.key)

        #Diseñamos la camida
        disenar_comida(tamano_cuadrado, comida_x, comida_y)

        #Actualizamos la posicion de la serpiente
        x += velocidad_x
        y += velocidad_y
        #Diseñamos la serpiente
        pixels.append([x, y]) #append concatena
        if len(pixels) > tamano_serpiente:
            del pixels[0]
        
        #Si la serpiente choca con su propio cuerpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fin_juego = True #Entonces termina el juego
        
        disenar_serpiente(tamano_cuadrado, pixels)
        #Diseñamos los puntos de vida
        disenar_puntuacion(tamano_serpiente - 1)
        #Actualizamos la pantalla
        pygame.display.update()

        #Crear una nueva comida
        if x== comida_x and y==comida_y:
            tamano_serpiente += 1
            comida_x, comida_y = generar_comida()

        reloj.tick(velocidad_juego)

#Esto es lo primero que va a leer el python
if __name__ == "__main__":
    correr_juego() #Se ejecuta mi juego
    pygame.quit() #Con esto me salgo del juego