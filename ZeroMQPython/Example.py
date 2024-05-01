#! /usr/bin/env python
import sys
import zmq






####################################
# Open Port
####################################
port = "8080"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

####################################
# Socket to talk to server
####################################
context = zmq.Context()
socket = context.socket(zmq.SUB)
print("Collecting updates from server...")
socket.connect("tcp://localhost:%s" % port)

####################################
# Subscribe to temperature
####################################
topicfilter = b"test"
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)



####################################
# Process
####################################
while True:
    string = socket.recv()
    print("%s" % string)