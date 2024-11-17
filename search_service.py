import json
import zmq
import time

USER_DATA = 'user_data.json'


def load_data():
    """Loads user data from JSON file"""
    with open(USER_DATA, 'r') as file:
        return json.load(file)


def search_recipes(data, search_term, search_by):
    """Searches for recipes based on title or ingredients."""
    results = []
    for user, recipes in data.items():
        for recipe in recipes:
            if (search_by == 'title' and search_term in recipe['name']) or \
                    (search_by == 'ingredient' and search_term in recipe['ingredients']):
                results.append({
                    'user': user,
                    'name': recipe['name'],
                    'ingredients': recipe['ingredients'],
                    'instructions': recipe['instructions']
                })
    return results


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("Search service started. Listening for requests...")
    while True:
        # Receive request
        message = socket.recv_json()
        search_term = message.get('search_term')
        search_by = message.get('search_by')

        print("Processing search request...")  # Message to show it's working
        time.sleep(2)  # Delay to show process

        # Load data and search
        user_data = load_data()
        results = search_recipes(user_data, search_term, search_by)

        # Send response
        socket.send_json(results)


if __name__ == "__main__":
    main()
