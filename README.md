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

# Set up a ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")  # Connect to the microservice

# Define the search parameters
search_params = {
    'search_term': 'chicken',  # The search term (e.g., title or ingredient)
    'search_by': 'ingredient'  # Either 'title' or 'ingredient'
}

# Send the search request to the microservice
socket.send_json(search_params)

# Wait for the response from the microservice
response = socket.recv_json()

# Print the search results
print("Search Results:")
for recipe in response:
    print(f"\nRecipe Name: {recipe['name']}")
    print(f"Ingredients: {recipe['ingredients']}")
    print(f"Instructions: {recipe['instructions']}")
```

## RECEIVING DATA:
To receive data from the Search Microservice, you need to set up a ZeroMQ REP socket on the microservice that listens for requests from the client, processes them, and sends back the response.

Steps to Receive Data:

1. The microservice listens for incoming JSON requests.
2. It processes the request by searching the data (user_data.json) based on the provided search parameters (search_term and search_by).
3. The microservice sends back a JSON array containing the results of the search (recipes that match the criteria).
```python
# Receive the request from the client
message = socket.recv_json()  # Receive JSON message from client
search_term = message.get('search_term')  # Extract the search term
search_by = message.get('search_by')  # Extract the search criterion (title or ingredient)
```
The microservice listens on port 5555 for incoming requests.
When it receives a request (e.g., search term 'chicken' and search by 'ingredient'), it processes the search and returns the matching recipes.

## UML DIAGRAM
![UML Sequence Diagram]
(https://github.com/phanr8541/recipe_microserviceA/blob/main/UML%20Sequence%20Diagram.JPG)
