import Model.ClModel


class ModelGenerator:
    def __init__(self,
                 zmq: int = 9090,
                 db: int = 9090):
        self.zmq = zmq
        self.db = db

        #Classification Model Factory
        self.clsModelFectory = dict()
        self.clsModelFectory["test"] = Model.ClModel

        self.modelFactory = dict()
        self.modelFactory["cls"] = self.clsModelFectory

    def generate(self,
                 type:str="",
                 name:str="",
                 mode:str="",
                 hyper:str=""):

        model = self.modelFactory[type][name](port=self.zmq,
                                              bypass=False)
        return model












