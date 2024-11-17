Microservice Communication
My unit converter service communicates via ZeroMQ and the microservice binds to port 5555. You must install ZeroMQ before using this microservice and include 'import zmq' in your main program. If you need to, you can change the port the microservice binds to incase it is already in use.

Files
unit_converter_service.py is the microservice
converter_example.py is the test program shown in the video
