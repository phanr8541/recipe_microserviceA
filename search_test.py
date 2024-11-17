import json
import os
import zmq
import time

USER_DATA = 'user_data.json'

title = "Search Recipe - Test Main Program"
print(title)
print("------------------------------------------")
def load_data():
    """Loads existing JSON or creates new JSON"""
    if os.path.exists(USER_DATA):
        with open(USER_DATA, 'r') as file:
            return json.load(file)
    else:
        with open(USER_DATA, 'w') as file:
            json.dump({}, file)
        return {}


def save_data(data):
    """Saves data to user_data.json"""
    with open(USER_DATA, 'w') as file:
        json.dump(data, file, indent=4)


def login():
    """Enter a username"""
    user_data = load_data()
    username = input("Please enter your username: ")
    if username not in user_data:
        print(f"Username not found. A new account for '{username}' will be created.")
        user_data[username] = []
        save_data(user_data)
    return username


def add_recipe(username):
    """Add a recipe"""
    user_data = load_data()

    recipe_name = input("Enter the recipe name: ")
    ingredients = input("Enter ingredients (comma separated): ")
    instructions = input("Enter instructions: ")

    recipe = {
        'name': recipe_name,
        'ingredients': ingredients.split(','),
        'instructions': instructions
    }

    user_data[username].append(recipe)
    save_data(user_data)
    print('Recipe successfully added!')


def search_recipes(username):
    """Search recipes by title or ingredients"""
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    search_by = input('Search by "title" or "ingredient": ').strip().lower()
    if search_by not in ['title', 'ingredient']:
        print("Invalid option. Please enter 'title' or 'ingredient'.")
        return

    search_term = input(f'Enter the {search_by} to search for: ').strip()

    socket.send_json({'search_term': search_term, 'search_by': search_by})
    print("Searching for recipes. Please wait...")
    results = socket.recv_json()
    time.sleep(0.5)  # Short delay for readability

    if results:
        print("\nSearch Results:")
        for i, recipe in enumerate(results, start=1):
            print(f"\nRecipe {i}:")
            print(f"  Name: {recipe['name']}")
            print(f"  Ingredients: {recipe['ingredients']}")
            print(f"  Instructions: {recipe['instructions']}")
    else:
        print("No matching recipes found.")


def main():
    """Main function to login and interact with recipes"""
    username = login()

    while True:
        action = input(
            f"\nHello {username}! Enter 'add' to add a recipe, 'search' to search recipes, or 'exit' to exit: ").lower()

        if action == 'add':
            add_recipe(username)
        elif action == 'search':
            search_recipes(username)
        elif action == 'exit':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == '__main__':
    main()
