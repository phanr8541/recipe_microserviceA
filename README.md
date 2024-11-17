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
To request data from the Search Microservice, you need to send a JSON message with the search parameters (search_term and search_by) to the microservice using the ZeroMQ (zmq) REQ-REP pattern.

Steps to Request Data:
1. Set up a client using the zmq.REQ socket.
2. Send a JSON object with two key-value pairs:
- search_term: The term you want to search for (either a recipe title or an ingredient).
- search_by: Whether you want to search by "title" or "ingredient".
The client will send the request to the microservice, which will process it and return the results.
```python
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
```
