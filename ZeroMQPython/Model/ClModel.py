import zmq
import json


class ClModel:
    def __init__(self,
                 port=9090,
                 bypass=False):
        self.bypass = bypass
        if self.bypass == False:
            context = zmq.Context()
            self.socket = context.socket(zmq.PUB)
            self.socket.bind("tcp://localhost:%s" % port)


    def updateTotalEpoch(self, total_epoch=0):
        if self.bypass == True:
            return
        jsonObject = {'name': 'totalEpoch', 'total_epoch': total_epoch}
        jsonContent = json.dumps(jsonObject)
        self.socket.send_unicode(jsonContent)

    def updateTotalBatch(self, total_batch=0):
        if self.bypass == True:
            return
        jsonObject = {'name': 'totalBatch', 'total_batch': total_batch}
        jsonContent = json.dumps(jsonObject)
        self.socket.send_unicode(jsonContent)

    def updateAvgBatchError(self, error=0.0):
        if self.bypass == True:
            return
        jsonObject = {'name': 'batchAvgError', 'error': error}
        jsonContent = json.dumps(jsonObject)
        self.socket.send_unicode(jsonContent)

    def updateCurrentEpoch(self, epoch):
        if self.bypass == True:
            return
        jsonObject = {'name': 'currentEpoch', 'epoch': epoch}
        jsonContent = json.dumps(jsonObject)
        self.socket.send_unicode(jsonContent)

    def updateCurrentBatch(self, batch):
        if self.bypass == True:
            return
        jsonObject = {'name': 'currentBatch', 'batch': batch}
        jsonContent = json.dumps(jsonObject)
        self.socket.send_unicode(jsonContent)

    def trainEnd(self):
        if self.bypass == True:
            return
        jsonObject = {'name': 'trainEnd'}
        jsonContent = json.dumps(jsonObject)
        self.socket.send_unicode(jsonContent)

    def train(self):
        raise NotImplementedError()

    def test_debug(self, test):
        self.socket.send_unicode(test)





