import requests
def get_joke(category):
    url = f"https://v2.jokeapi.dev/joke/{category}?type=single"
    response = requests.get(url)
    data = response.json()
    return data['joke'] if 'joke' in data else "No joke found for this category"

if __name__ == "__main__":
    while True:
        category = input("Enter a joke category (Any, Misc, Programming, Dark, Pun, Spooky, Christmas) or x to exit: ")
        if category not in "Xx":
            joke = get_joke(category)
            print(joke)
        else:
            print("Thanks for playing")
            break

