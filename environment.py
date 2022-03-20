class Environment:
    def __init__(self):
        self.lum=10

    def modify_lum(self,valor):
        self.lum+=valor

    def set_lum(self,valor):
        self.lum=valor

    def get_lum(self):
        return self.lum

    def __str__(self):

        status="El nivel de luz es de " + str(self.lum) + " Lux"
        return status