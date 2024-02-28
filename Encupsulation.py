class Car:
    def __init__(self,make,model):
        self._make = make
        self._model = model

    def set_make(self,make):
        self._make = make

    def set_model(self,model):
        self._model = model

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model