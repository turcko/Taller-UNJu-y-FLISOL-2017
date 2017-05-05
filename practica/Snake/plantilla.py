import pygame

class SceneBase():
    def __init__(self):
        self.next = self

    def ProcessInputs(self, evento):
        pass

    def Render(self, screen):
        pass

    def SwitchToScene(self, scene):
        self.next = scene

    def Terminate(self):
        self.SwitchToScene(None)

class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInputs(self, evento):
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
            self.SwitchToScene(GameScene())

    def Render(self, screen):
        screen.fill((0,150,0))

class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInputs(self, evento):
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
            self.SwitchToScene(TitleScene())

    def Render(self, screen):
        screen.fill((0,0,150))

def game_run(ancho, alto, fps, starting_scene):
    screen = pygame.display.set_mode((ancho, alto))
    active_scene = starting_scene

    while active_scene != None:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                active_scene.Terminate()
            active_scene.ProcessInputs(evento)

        active_scene.Render(screen)
        active_scene = active_scene.next #¿POR QUE NO SE PUEDE INVOCAR ANTES DEL Render?

        pygame.time.delay(fps)
        pygame.display.flip()

game_run(600,600,50,TitleScene())