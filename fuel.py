from engine import *

class Fuel():
    def __init__(self,engine):
        self.level=1000
        self.engine=engine
        

    def update(self):
        speed=self.engine.get_speed()
        return self.level-abs(speed)*0.01

    def __str__(self):

        status="El nivel de combustible es de " + str(self.update()) + " L"
        print("---------------------------------------------------------------------------------")
        return status

