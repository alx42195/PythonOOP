import random
import json

numbers = [random.random() for _ in range(100)]

with open("random.json", "w") as file:
    json.dump(numbers, file)

