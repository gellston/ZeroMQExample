
from time import sleep

from Model.clsModel import clsModel


clsModoelFactory = dict()
clsModoelFactory["test"] = clsModel



template = clsModoelFactory["test"]
model = template(port=9090,
                 bypass=False)



#### Hyper Parameter
total_epoch = 100
total_batch = 50
#### Hyper Parameter

####################################
# Process
####################################

print('train start')

model.updateTotalEpoch(total_epoch)
for epoch in range(total_epoch):
    print('current epoch=', epoch)
    model.updateCurrentEpoch(epoch)

    model.updateTotalBatch(total_batch)
    for batch in range(total_batch):
        print('current batch=', batch)
        model.updateCurrentBatch(batch)
        sleep(0.05)

    model.updateAvgBatchError(1280)


model.trainEnd()






