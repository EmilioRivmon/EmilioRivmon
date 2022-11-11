

class agent:
    def __init__(self,env):
        self.env = env
        self.x = env.init_posX
        self.y = env.init_posY
        self.derecha = True
        self.posicionar()
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
    def posicionar(self):
        arriba = True
        izquierda = True
        while (arriba == True or izquierda == True):
            if (self.up() == False):
                arriba = False
            if (self.left() == False):
                izquierda = False
        print("Etapas Iniciales: ", self.env.steps)
        print("Agente posicionado en [0,0]")
    def comenzar(self):
        self.suck()
        while (self.env.steps != 1000):
            if (self.derecha == True):
                x = self.right()
                if (x == False):
                    x = self.down()
                    if (x == False):
                        # La aspiradora llegó al final
                        break
                    self.derecha = False
                    self.suck()
                    continue
                self.suck()
            else:
                x = self.left()
                if (x == False):
                    x = self.down()
                    if (x == False):
                        # La aspiradora llegó al final
                        break
                    self.derecha = True
                    self.suck()
                    continue
                self.suck()
            #self.env.print_environment()
        print("Limpieza finalizada")
        print("Performance obtenido: ", self.env.get_performance())
        print("Etapas: ", self.env.steps)
        print("Puntos: ", self.env.puntos)