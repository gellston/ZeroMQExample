import typer

from ModelGenerator import ModelGenerator

app = typer.Typer(add_completion=False, help="dolphin deep learning framework CLI")

@app.command(short_help="dl training command",
             help="this is deep learning  training command")
def train(type:str="",
          name:str="",
          mode:str="",
          hyper:str="",
          zmq:int=9090,
          db:int=9090,
          group:str="",
          out:str=""):

    generator = ModelGenerator(zmq=zmq, db=db)
    model = generator.generate(type=type, name=name, mode=mode, hyper=hyper)
    model.train(group, out)



@app.command(short_help="onnx convert command",
             help="this is onnx convert command")
def onnx(name:str="",
         group:str="",
         zmq:int=9090,
         db:int=9090,
         out:str=""):

    print(f"name : {name}")
    print(f"group : {group}")
    print(f"zmq : {zmq}")
    print(f"db : {db}")
    print(f"out : {out}")


if __name__ == "__main__":
    app()




"""
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


def main(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
"""


