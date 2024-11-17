# Microservice Communication
The recipe search service communicates with ZeroMQ and the microservice binds to port 5555. You can change the port that the microservice is binded to as needed to accommodate for other services.
## Prerequisites
ZeroMQ will need to be installed on your system before using the microservice
```bash
pip install zmq
```
## Files
search_service.py is the microservice
search_test.py is the test program shown in the video

## REQUESTING DATA:
First you will need zmq to communicate with the microservice and json to format the data. The client will connect to the server via the ZeroMQ request (REQ) socket. You should connect to the address where your microservice is bound (in this case tcp://localhost:5555).
'''python
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
'''
