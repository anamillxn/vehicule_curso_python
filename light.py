from environment import *

class Light:
    def __init__(self,environment):
        self.environment=environment
        self.activated=0

    def activate(self):
        self.activated=1

    def deactivate(self):
        self.activated=0

    def update(self):
        lum=self.environment.get_lum()

        if lum<40:
            self.activate()

        else:
            self.deactivate()
    
    def __str__(self):

        if self.activated==1:
            status="La luces están encendidas"

        else:
            status="La luces están apagadas"

        return status