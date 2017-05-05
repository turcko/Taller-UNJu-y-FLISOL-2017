import pygame
import sys
import random

tama = (600,600)
colorFondo = pygame.Color(0,0,0)
dimensionCuerpo = (30,30)
posicionInicialCuerpo = (0,30)
dimensionComida = 30,30
desplazamiento = dimensionCuerpo[0]

class Snake():
    def __init__(self):
        self.rect = pygame.Rect(posicionInicialCuerpo, dimensionCuerpo)
        self.direccion = "der"

    def dibujar(self, ventana): #1
        ventana.blit(self.imagen, self.rect)

    def mover(self, bandera): #2
        if bandera == 1:
            self.rect.top -= desplazamiento
        elif bandera == 2:
            self.rect.left += desplazamiento
        elif bandera == 3:
            self.rect.top += desplazamiento 
        elif bandera == 4:
            self.rect.left -= desplazamiento

    def pintar(self, ventana): #3
        ventana.fill(colorFondo, self.rect)

    def set_posicion(self, posicion):
        self.rect = posicion

    def girar(self, bandera): #4
        if self.direccion == "der":
            if bandera == 1:
                self.imagen = pygame.transform.rotate(self.imagen, 90)
                self.direccion = "arr"
            if bandera == 3:
                self.imagen = pygame.transform.rotate(self.imagen, -90)
                self.direccion = "aba"
        elif self.direccion == "izq":
            if bandera == 1:
                self.imagen = pygame.transform.rotate(self.imagen, -90)
                self.direccion = "arr"
            if bandera == 3:
                self.imagen = pygame.transform.rotate(self.imagen, 90)
                self.direccion = "aba"
        elif self.direccion == "arr":
            if bandera == 2:
                self.imagen = pygame.transform.rotate(self.imagen, -90)
                self.direccion = "der"
            if bandera == 4:
                self.imagen = pygame.transform.rotate(self.imagen, 90)
                self.direccion = "izq"
        elif self.direccion == "aba":
            if bandera == 2:
                self.imagen = pygame.transform.rotate(self.imagen, 90)
                self.direccion = "der"
            if bandera == 4:
                self.imagen = pygame.transform.rotate(self.imagen, -90)
                self.direccion = "izq"

    def get_posicion(self):
        return self.rect

class Cabeza(Snake):
    def __init__(self):
        Snake.__init__(self)
        self.imagen = pygame.image.load("cabeza.png")

    def choque(self, cuerpo):
        if self.rect.top < dimensionCuerpo[0] or self.rect.bottom > tama[1] or self.rect.left < 0 or self.rect.right > tama[1]:
            return True
        for parte in cuerpo:
            if self.rect.colliderect(parte.get_posicion()):
                return True

    def come(self, comida):
        return self.rect.colliderect(comida.get_posicion())

    def reiniciar_posicion_y_direccion(self):
        if self.direccion == "izq":
            self.imagen = pygame.transform.rotate(self.imagen, 180)
        elif self.direccion == "arr":
            self.imagen = pygame.transform.rotate(self.imagen, -90)
        elif self.direccion == "aba":
            self.imagen = pygame.transform.rotate(self.imagen, 90)
        self.direccion = "der"
        rectAux = pygame.Rect(posicionInicialCuerpo, dimensionCuerpo)
        self.set_posicion(rectAux)

class Comida():
    def __init__(self):
        self.imagen = pygame.image.load("manzana.png")
        ubiacionComida = random.randint(0,(tama[0]/dimensionComida[0])-1)*dimensionComida[0], random.randint(0,(tama[1]/dimensionComida[1])-1)*dimensionComida[1]
        self.rect = pygame.Rect(ubiacionComida ,dimensionComida)

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.rect)

    def pintar(self, ventana):
        ventana.fill(colorFondo, self.rect)

    def get_posicion(self):
        return self.rect

    def redefinir_posicion(self):
        ubiacionComida = (random.randint(0,(tama[0]/dimensionComida[0])-1)*desplazamiento , random.randint(1,(tama[1]/dimensionComida[1])-1)*desplazamiento)
        self.rect = pygame.Rect(ubiacionComida ,dimensionComida)

class Cola(Snake):
    def __init__(self):
        Snake.__init__(self)
        self.imagen = pygame.image.load("colaSnake.png")