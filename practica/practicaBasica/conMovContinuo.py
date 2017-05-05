import pygame as pg
import sys

colorFondo = pg.Color(0,0,0)
tama = 600,600
ventana = pg.display.set_mode(tama)

sentido = "arr"

obj1 = pg.image.load("nave.png")
obj1 = pg.transform.scale(obj1, (150,150))

obj2 = pg.image.load("nave.png")
obj2 = pg.transform.scale(obj2, (150,150))

desplazamiento = 5
rectObj1 = obj1.get_rect()
rectObj2 = obj2.get_rect()
rectObj2.left = 200
rectObj2.top = 200

teclaUp = False
teclaDown = False
teclaLeft = False
teclaRight = False

while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            sys.exit("Cierre por x")
            pg.quit()
        elif evento.type == pg.KEYDOWN:
            if evento.key == pg.K_ESCAPE:
                sys.exit("Cierre por escape")
                pg.quit()
            if evento.key == pg.K_UP:
                teclaUp = True
                if sentido == "aba":
                    obj1 = pg.transform.rotate(obj1, 180)
                elif sentido == "izq":
                    obj1 = pg.transform.rotate(obj1, -90)
                elif sentido == "der":
                    obj1 = pg.transform.rotate(obj1, 90)
                sentido = "arr"

            if evento.key == pg.K_DOWN:
                teclaDown = True
                if sentido == "arr":
                    obj1 = pg.transform.rotate(obj1, 180)
                elif sentido == "izq":
                    obj1 = pg.transform.rotate(obj1, 90)
                elif sentido == "der":
                    obj1 = pg.transform.rotate(obj1, -90)
                sentido = "aba"

            if evento.key == pg.K_LEFT:
                teclaLeft = True
                if sentido == "aba":
                    obj1 = pg.transform.rotate(obj1, -90)
                elif sentido == "arr":
                    obj1 = pg.transform.rotate(obj1, 90)
                elif sentido == "der":
                    obj1 = pg.transform.rotate(obj1, 180)
                sentido = "izq"

            if evento.key == pg.K_RIGHT:
                teclaRight = True
                if sentido == "aba":
                    obj1 = pg.transform.rotate(obj1, 90)
                elif sentido == "arr":
                    obj1 = pg.transform.rotate(obj1, -90)
                elif sentido == "izq":
                    obj1 = pg.transform.rotate(obj1, 180)
                sentido = "der"

        elif evento.type == pg.KEYUP:
            if evento.key == pg.K_UP:
                teclaUp = False
            if evento.key == pg.K_DOWN:
                teclaDown = False
            if evento.key == pg.K_LEFT:
                teclaLeft = False
            if evento.key == pg.K_RIGHT:
                teclaRight = False
    
    if teclaUp:
        rectObj1.top -= desplazamiento
    if teclaDown:
        rectObj1.top += desplazamiento
    if teclaLeft:
        rectObj1.left -= desplazamiento
    if teclaRight:
        rectObj1.left += desplazamiento

    # if rectObj1.left <= 0 or rectObj1.right >= tama[1]:
    #     desplazamiento *= -1

    # rectObj1 = rectObj1.move(desplazamiento, 0)

    ventana.fill(colorFondo)
    ventana.blit(obj1, rectObj1)
    ventana.blit(obj2, rectObj2)

    if rectObj1.colliderect(rectObj2):
        print("Choque")

    pg.time.delay(25)
    pg.display.flip()