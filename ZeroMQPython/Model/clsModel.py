import sys
import zmq

class clsModel:
    def __init__(self,
                 dest="tcp://localhost:8080",
                 bypass=False):
        self.bypass = bypass
        if self.bypass == False:
            context = zmq.Context()
            socket = context.socket(zmq.SUB)
            socket.connect(dest)
            print("connection to ")

    def updateEpochInfo(self, epoch=0, total_epoch=0):
        if self.bypass == True:
            return
        print('test')

    def updateBatchInfo(self, batch=0, total_batch=0):
        if self.bypass == True:
            return
        print('test')

    def updateBatchError(self, error=0.0):
        if self.bypass == True:
            return
        print('test')

    def trainEnd(self):
        if self.bypass == True:
            return
        print('test')

    def train(self):
        raise NotImplementedError()





