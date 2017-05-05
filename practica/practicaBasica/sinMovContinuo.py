import pygame as pg
import sys

colorFondo = pg.Color(0,0,0)
tama = 600,600
ventana = pg.display.set_mode(tama)
pg.display.set_caption("Ventana 1")

imagen = pg.image.load("nave.png")
imagen2 = pg.image.load("nave.png")

imagen = pg.transform.scale(imagen, (100,100))
imagen2 = pg.transform.scale(imagen2, (100,100))

rectImgen = imagen.get_rect()
rectImagen2 = imagen2.get_rect()
rectImagen2.left = 200

desplazamiento = 5
sentido = "arr"

while True:
    for evento in pg.event.get():        
        if evento.type == pg.QUIT:
            sys.exit("Clic en X")
            pg.quit()
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_ESCAPE:
                sys.exit("Escape")
                pg.quit()
            elif evento.key == pg.K_DOWN:
                if sentido == "arr":
                    imagen = pg.transform.rotate(imagen, 180)
                elif sentido == "der":
                    imagen = pg.transform.rotate(imagen, -90)
                elif sentido == "izq":
                    imagen = pg.transform.rotate(imagen, +90)
                sentido = "aba"
                rectImgen.top += desplazamiento
            elif evento.key == pg.K_UP:
                if sentido == "aba":
                    imagen = pg.transform.rotate(imagen, 180)
                elif sentido == "der":
                    imagen = pg.transform.rotate(imagen, 90)
                elif sentido == "izq":
                    imagen = pg.transform.rotate(imagen, -90)
                sentido = "arr"
                rectImgen.top -= desplazamiento
            elif evento.key == pg.K_LEFT:
                if sentido == "arr":
                    imagen = pg.transform.rotate(imagen, 90)
                elif sentido == "der":
                    imagen = pg.transform.rotate(imagen, 180)
                elif sentido == "aba":
                    imagen = pg.transform.rotate(imagen, -90)
                sentido = "izq"
                rectImgen = rectImgen.move(-desplazamiento,0)
            elif evento.key == pg.K_RIGHT:
                if sentido == "arr":
                    imagen = pg.transform.rotate(imagen, -90)
                elif sentido == "izq":
                    imagen = pg.transform.rotate(imagen, 180)
                elif sentido == "aba":
                    imagen = pg.transform.rotate(imagen, 90)
                sentido = "der"
                rectImgen = rectImgen.move(+desplazamiento, 0)

    ventana.fill(colorFondo)
    ventana.blit(imagen, rectImgen)
    ventana.blit(imagen2, rectImagen2)
    
    if rectImgen.colliderect(rectImagen2):
        print("Choque")

    pg.time.delay(25)
    pg.display.flip()