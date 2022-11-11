import random
import numpy as np
import os
import time
class env:
    steps = 0
    puntos = 0
    # 0 = limpio
    # 1 = sucio
    # 2 = aspiradora
    def __init__ (self,sizeX,sizeY,init_posX,init_posY,dirt_rate):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.m = np.zeros((sizeX,sizeY))
        tamaño = sizeX*sizeY
        self.init_posX = init_posX
        self.init_posY = init_posY
        self.dirtSlotsAmount = (dirt_rate * tamaño)/100
        self.m[init_posX][init_posY] = 2
        for i in range (0,sizeX):
            for j in range(0,sizeY):
                self.m[i][j] = 0
        i = 0
        while (i < self.dirtSlotsAmount):
            slotX = random.randint(0,self.sizeX-1)
            slotY = random.randint(0,self.sizeY-1)
            if (self.m[slotX][slotY] == 0):
                self.m[slotX][slotY] = 1
                print(i ," de ", self.dirtSlotsAmount)
                i = i + 1
        print("Ambiente generado")
    def accept_action(self,action,x,y):
        # arriba abajo izquierda derecha limpiar nohacernada
        if (action == "arriba"):
            if (x-1 >= 0):
                self.steps = self.steps + 1
                return True
            return False
        elif (action == "abajo"):
            if (x+1 < self.sizeX):
                self.steps = self.steps + 1
                return True
            return False
        elif (action == "izquierda"):
            if (y-1 >= 0):
                self.steps = self.steps + 1
                return True
            return False
        elif (action == "derecha"):
            if (y+1 < self.sizeY):
                self.steps = self.steps + 1
                return True
            return False
        elif (action == "limpiar"):
            if (self.is_dirty(x,y) == True):
                self.puntos = self.puntos + 1
                self.steps = self.steps + 1
                self.m[x][y] = 0
        else:
            self.steps = self.steps + 1
    def is_dirty(self,x,y):
        #print("intentando limpiar en ", x , " ", y)
        if (self.m[x][y] == 1):
            return True
        return False
    def get_performance(self):
        return self.puntos/self.steps
    def print_environment(self):
        print('\n'*5)
        for a in range(0,self.sizeX):
            for b in range(0,self.sizeY):
                print("|",int(self.m[a][b]),end=' ')
            print("|")




