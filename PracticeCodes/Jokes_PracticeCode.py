import requests
import random

jokeAbout = "women"
url = f"https://icanhazdadjoke.com/search?term={jokeAbout}"  # Replace with the desired joke ID if needed
headers = {"Accept": "application/json"}  # Specify JSON format for response

response = requests.get(url, headers=headers)

print(len(response.json()["results"]))
# data = dict(response.json())
# # print(data.keys())
# # print(data["results"])
#
# if len(data["results"]) == 0:
#     print("No Jokes found for this topic, please search for another topic")
# else:
#     # lenOfResults = len(data["results"])
#     randomList = random.choice(data["results"])
#     print(randomList["joke"])


# # Random Jokes
#
# url = "https://icanhazdadjoke.com/"
# headers = {"Accept": "application/json"}
#
# response = requests.get(url, headers=headers)
# print(response.json()["joke"])
#
print(random.choice([]))