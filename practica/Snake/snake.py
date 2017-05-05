from clases import *

class SceneBase():
    def __init__(self):
    	self.next = self

    def ProcessInput(self, events):
        pass

    def Update(self):
        pass

    def Render(self, screen):
        pass

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.next = None

class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.bandera = 0
        self.imagen1 = pygame.image.load("portada.png")
        self.imagen2 = pygame.image.load("portada2.png")

    def ProcessInput(self, events):
        for evento in events:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                self.SwitchToScene(GameScene())

    def Render(self, screen):
        if self.bandera == 0:
            screen.blit(self.imagen1, (0,0))
            self.bandera = 1
        else:
            screen.blit(self.imagen2, (0,0))
            self.bandera = 0

class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.banderaDesplazamiento = 0
        self.cola = []
        self.puntaje = 0
        self.cabeza = Cabeza()
        self.comida = Comida()
        self.fuente = pygame.font.SysFont("Arial", 14)

    def ProcessInput(self, events):
        for evento in events:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    self.SwitchToScene(TitleScene())
                elif evento.key == pygame.K_UP and self.banderaDesplazamiento != 3:
                    self.banderaDesplazamiento = 1
                elif evento.key == pygame.K_RIGHT and self.banderaDesplazamiento != 4:
                    self.banderaDesplazamiento = 2
                elif evento.key == pygame.K_DOWN and self.banderaDesplazamiento != 1:
                    self.banderaDesplazamiento = 3
                elif evento.key == pygame.K_LEFT and self.banderaDesplazamiento != 2:
                    self.banderaDesplazamiento = 4
                self.cabeza.girar(self.banderaDesplazamiento)

    def Render(self, screen):
        if self.banderaDesplazamiento == 0:
            screen.fill(colorFondo)
        
        screen.fill(colorFondo, (0,0, tama[0], dimensionCuerpo[0]-10))
        screen.blit(self.fuente.render(":.. Puntaje: ..: " + str(self.puntaje), 0, (255,255,255)), (400, 0))
        pygame.draw.line(screen, (255,255,255), (0, dimensionCuerpo[0]-1), (tama[0], dimensionCuerpo[0]-1))

        if self.banderaDesplazamiento != 0:
            posicionAux = pygame.Rect(self.cabeza.get_posicion())
            self.cabeza.pintar(screen)
            self.cabeza.mover(self.banderaDesplazamiento)

            if self.cabeza.choque(self.cola):
                self.reiniciar_juego()

            if self.cabeza.come(self.comida):
                self.comida.pintar(screen)
                self.comida.redefinir_posicion()
                
                self.cola.append(Cola())
                self.puntaje += 1

            if len(self.cola) > 0:
                self.cola[0].pintar(screen)
                self.cola[0].girar(self.banderaDesplazamiento)
                self.cola[0].set_posicion(posicionAux)
                self.cola[0].dibujar(screen)
                self.cola.append(self.cola[0])
                self.cola.pop(0)

        self.comida.dibujar(screen)
        self.cabeza.dibujar(screen)        

    def reiniciar_juego(self):
        self.banderaDesplazamiento = 0        
        self.cola = []
        self.cabeza.reiniciar_posicion_y_direccion()
        self.comida.redefinir_posicion()
        self.puntaje = 0



def run_game(ancho, alto, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((ancho,alto))

    active_scene = starting_scene

    while active_scene != None:
        events_filter = []
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    active_scene.Terminate()
                elif evento.key == pygame.K_u and fps < 100:
                    fps -= 10
                elif evento.key == pygame.K_j and fps > 50:
                    fps += 10
                else:
                    events_filter.append(evento)

        active_scene.ProcessInput(events_filter)
        active_scene.Update()
        active_scene.Render(screen)

        active_scene = active_scene.next

        pygame.display.flip()
        pygame.time.delay(fps)

run_game(600, 600, 100, TitleScene())