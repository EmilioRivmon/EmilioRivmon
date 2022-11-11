import random

class agent:
    def __init__(self,env):
        self.env = env
        self.x = env.init_posX
        self.y = env.init_posY
        self.comenzar()
    def up(self):
        x = self.env.accept_action("arriba",self.x,self.y)
        if (x == True):
            self.x = self.x-1
            return True
        return False
    def down(self):
        x = self.env.accept_action("abajo", self.x,self.y)
        if (x == True):
            self.x = self.x+1
            return True
        return False
    def left(self):
        x = self.env.accept_action("izquierda", self.x,self.y)
        if (x == True):
            self.y = self.y-1
            return True
        return False
    def right(self):
        x = self.env.accept_action("derecha", self.x,self.y)
        if (x == True):
            self.y = self.y+1
            return True
        return False
    def suck(self):  # Limpia
        self.env.accept_action("limpiar", self.x,self.y)
    def idle(self):  # no hace nada
        self.env.accept_action("nada", self.x,self.y)
    def comenzar(self):
        self.suck()
        while (self.env.steps != 1000):
            rand = random.randint(0,3)
            if(self.env.puntos >= int(self.env.dirtSlotsAmount)):
                # La aspiradora limpió correctamente.
                break
            if (rand == 0): # arriba

                x = self.up()

                if (x == True):
                    self.suck()
            elif (rand == 1): # abajo
                x = self.down()

                if (x == True):
                    self.suck()
            elif (rand == 2):  # izquierda
                x = self.left()

                if (x == True):
                    self.suck()
            else: # derecha
                x = self.right()

                if (x == True):
                    self.suck()
        print("Cantidad de slots sucios: " , int(self.env.dirtSlotsAmount))
        print("Tiempo Obtenido: ", self.env.get_performance())
        print("Movimientos Realizados: ", self.env.puntos)
